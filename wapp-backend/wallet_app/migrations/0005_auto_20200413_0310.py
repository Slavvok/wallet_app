# Generated by Django 3.0.5 on 2020-04-13 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_app', '0004_auto_20200412_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addtransaction',
            name='id',
            field=models.CharField(default=0, editable=False, max_length=64, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subtracttransaction',
            name='id',
            field=models.CharField(default=0, editable=False, max_length=64, primary_key=True, serialize=False),
        ),
    ]
