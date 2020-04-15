from django.db import models
import uuid


def generate_id():
    return uuid.uuid4().hex


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
    commentary = models.TextField('комментарий', max_length=120, default='', null=True)
    wallet_id = models.ForeignKey(Wallet, verbose_name='кошелек',
                                  related_name='transactions', on_delete=models.CASCADE)

    id = models.CharField(primary_key=True,
                          default=generate_id, editable=False, max_length=64)
    type = models.CharField("тип транзакции", max_length=3, default='', editable=False)
    post_trans_value = models.FloatField('значение после транзакции', editable=False, default=None, null=True)

    def __str__(self):
        return f"{self.date} {self.value}"

    class Meta:
        ordering = ["-date"]

    def set_type(self):
        self.type = self.__class__.__name__[:3].lower()


class AddTransaction(Transaction):
    class Meta:
        proxy = True


class SubtractTransaction(Transaction):
    class Meta:
        proxy = True
