from django.urls import path, include
from rest_framework import routers
from .views import SubTransactionViewSet, AddTransactionViewSet, WalletViewSet, TransactionViewSet

router = routers.DefaultRouter()
router.register('wallets', WalletViewSet)
router.register('transactions', TransactionViewSet)
router.register('add-transaction', AddTransactionViewSet)
router.register('sub-transaction', SubTransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
