from django.db import models
import uuid


class Wallet(models.Model):
    name = models.CharField('название', max_length=60)
    value = models.FloatField('сумма', max_length=10, editable=False, default=0)
    currency = models.CharField('валюта', default='₽', max_length=10)

    def __str__(self):
        return f"{self.name} {self.value}"


class Transaction(models.Model):
    """транзакция"""
    date = models.DateTimeField('дата', auto_now=True)
    value = models.FloatField('сумма', max_length=10, default=0)
    commentary = models.TextField('комментарий', max_length=120, null=True, default=None)
    wallet_id = models.ForeignKey(Wallet, verbose_name='кошелек',
                                  related_name='transaction', on_delete=models.CASCADE)

    id = models.CharField(primary_key=True,
                          default=0, editable=False, max_length=64)
    post_trans_value = models.FloatField('значение после транзакции', editable=False, default=None, null=True)

    def save(self, *args, **kwargs):
        # Unique id with operation prefix
        self.id = self.__class__.__name__[0].lower() + uuid.uuid4().hex
        super().save(self, *args, **kwargs)

    def __str__(self):
        return f"{self.date} {self.value}"

    class Meta:
        abstract = True


class AddTransaction(Transaction):
    """перевод"""
    wallet_id = models.ForeignKey(Wallet, verbose_name='кошелек',
                                  related_name='add_transactions', on_delete=models.CASCADE)


class SubtractTransaction(Transaction):
    """списание"""
    wallet_id = models.ForeignKey(Wallet, verbose_name='кошелек',
                                  related_name='sub_transactions', on_delete=models.CASCADE)
