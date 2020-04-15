from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class TransactionSerializer(serializers.ModelSerializer):
    commentary = serializers.CharField(allow_blank=True, allow_null=True)

    def _operation(self, wallet_value, trans_value):
        return wallet_value

    def create(self, validated_data):
        transaction = self.Meta.model(
                value=validated_data['value'],
                commentary=validated_data['commentary'],
                wallet_id=validated_data['wallet_id'])
        wallet = validated_data['wallet_id']
        wallet.value = self._operation(wallet.value, transaction.value)
        transaction.post_trans_value = wallet.value
        transaction.set_type()
        transaction.save()
        wallet.save()
        return transaction

    class Meta:
        model = Transaction
        allow_null = True
        fields = ('date', 'type', 'value', 'post_trans_value', 'commentary', 'id', 'wallet_id')


class AddTransactionSerializer(TransactionSerializer):
    def _operation(self, wallet_value, trans_value):
        return wallet_value + trans_value

    class Meta:
        model = AddTransaction
        fields = TransactionSerializer.Meta.fields


class SubtractTransactionSerializer(TransactionSerializer):
    def _operation(self, wallet_value, trans_value):
        return wallet_value - trans_value

    class Meta:
        model = SubtractTransaction
        fields = TransactionSerializer.Meta.fields


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('id', 'name', 'value')


class WalletTransactionsSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True)

    class Meta:
        model = Wallet
        fields = ('name', 'value', 'transactions', 'transactions')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = ('url', 'username', 'email')
