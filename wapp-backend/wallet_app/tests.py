from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class AccountTests(APITestCase):
    def setUp(self):
        self.user_data = {
            'username': 'test',
            'password': 'test_test'
        }
        self.jwt_auth()

    def jwt_auth(self):
        url = reverse('api_token_auth')
        User.objects.create_superuser(username='test', email='test@test.com', password='test_test')
        response = self.client.post(url, self.user_data, format='json')
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION=f'JWT {token}')

    def test_post_wallet(self):
        data = {"name": "wallet"}
        response = self.client.post('/wallets/', data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_post_add_transactions(self):
        empty_comment_data = {"value": "2000", "wallet_id": "1", "commentary": ""}
        response1 = self.client.post('/add-transaction/', empty_comment_data, format='json')
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        data = {"value": "2000", "wallet_id": "1", "commentary": "dddd"}
        response2 = self.client.post('/add-transaction/', data, format='json')
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.data['post_trans_value'], 4000)

    # def test_post_sub_transactions(self):
        empty_comment_data = {"value": "2000", "wallet_id": "1", "commentary": ""}
        response1 = self.client.post('/sub-transaction/', empty_comment_data, format='json')
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        data = {"value": "2000", "wallet_id": "1", "commentary": "dddd"}
        response2 = self.client.post('/sub-transaction/', data, format='json')
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.data['post_trans_value'], 0)

    # def test_get_wallet_id_transactions(self):
        response = self.client.get('/wallets/1/transactions/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_wallets(self):
        response = self.client.get('/wallets/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_transactions(self):
        response = self.client.get('/transactions/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
