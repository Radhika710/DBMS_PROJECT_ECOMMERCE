# Generated by Django 4.2.7 on 2023-11-29 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_storetransaction_alter_order_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storetransaction',
            name='transaction_id',
            field=models.CharField(default=0, max_length=200, primary_key=True, serialize=False, unique=True),
        ),
    ]