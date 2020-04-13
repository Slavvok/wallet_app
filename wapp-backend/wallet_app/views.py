from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializers import WalletTransactionsSerializer, WalletSerializer, AddTransactionSerializer, SubtractTransactionSerializer
from django.db.models import Prefetch


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    @action(detail=True, methods=['get'])
    def transactions(self, request, pk=None):
        queryset = Wallet.objects.prefetch_related(
            Prefetch('add_transactions', AddTransaction.objects.order_by('-date')),
            Prefetch('sub_transactions', SubtractTransaction.objects.order_by('-date'))).filter(pk=pk).first()
        if queryset:
            serializer = WalletTransactionsSerializer(queryset)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class TransactionViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = AddTransactionSerializer
    queryset = AddTransaction.objects.filter() \
        .union(SubtractTransaction.objects.filter()) \
        .order_by('-date')


class AddTransactionViewSet(viewsets.ModelViewSet):
    serializer_class = AddTransactionSerializer
    queryset = AddTransaction.objects.all()


class SubTransactionViewSet(viewsets.ModelViewSet):
    serializer_class = SubtractTransactionSerializer
    queryset = SubtractTransaction.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
