# Generated by Django 3.1.2 on 2021-01-06 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bill', '0002_ordermodel_purchasemodel_salesmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesmodel',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
