from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class TransactionSerializer(serializers.ModelSerializer):

    # def create(self, validated_data):
    #     transaction = self.Meta.model(
    #         value=validated_data['value'],
    #         commentary=validated_data['commentary'],
    #         wallet_id=validated_data['wallet_id'])
    #     wallet = validated_data['wallet_id']
    #     transaction.save()
    #     self.Meta.model.change_value(wallet)
    #     return transaction

    class Meta:
        fields = ('date', 'value', 'post_trans_value', 'commentary', 'id', 'wallet_id')
        abstract = True


class AddTransactionSerializer(TransactionSerializer):

    def create(self, validated_data):
        transaction = self.Meta.model(
                value=validated_data['value'],
                commentary=validated_data['commentary'],
                wallet_id=validated_data['wallet_id'])
        wallet = validated_data['wallet_id']
        wallet.value += transaction.value
        wallet.save()
        transaction.post_trans_value = wallet.value
        transaction.save()
        return transaction

    class Meta:
        model = AddTransaction
        fields = TransactionSerializer.Meta.fields


class SubtractTransactionSerializer(TransactionSerializer):

    def create(self, validated_data):
        transaction = self.Meta.model(
                value=validated_data['value'],
                commentary=validated_data['commentary'],
                wallet_id=validated_data['wallet_id'])
        wallet = validated_data['wallet_id']
        wallet.value -= transaction.value
        wallet.save()
        transaction.post_trans_value = wallet.value
        transaction.save()
        return transaction

    class Meta:
        model = SubtractTransaction
        fields = TransactionSerializer.Meta.fields


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('id', 'name', 'value')


class WalletTransactionsSerializer(serializers.ModelSerializer):
    add_transactions = AddTransactionSerializer(many=True)
    sub_transactions = SubtractTransactionSerializer(many=True)

    class Meta:
        model = Wallet
        fields = ('name', 'value', 'add_transactions', 'sub_transactions')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = ('url', 'username', 'email')
