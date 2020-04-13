from django.contrib import admin
from .models import *


class WalletAdmin(admin.ModelAdmin):
    list_display = ['name', 'value', 'currency']


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['date', 'value', 'post_trans_value']


admin.site.register(Wallet, WalletAdmin)
admin.site.register(AddTransaction, TransactionAdmin)
admin.site.register(SubtractTransaction, TransactionAdmin)
