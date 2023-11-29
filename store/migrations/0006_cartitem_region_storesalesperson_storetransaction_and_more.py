# Generated by Django 4.2.7 on 2023-11-29 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_order_razor_pay_order_id_order_razor_pay_payment_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.BigIntegerField(null=True)),
            ],
            options={
                'db_table': 'store_cart',
            },
        ),
        migrations.CreateModel(
            name='region',
            fields=[
                ('Region_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Region_name', models.CharField(max_length=200, null=True)),
                ('RegionalManagerID', models.BigIntegerField(null=True)),
                ('TotalSales', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StoreSalesperson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salesperson_ID', models.BigIntegerField()),
                ('salesperson_name', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('job_title', models.TextField()),
                ('salary', models.IntegerField()),
            ],
            options={
                'db_table': 'store_salesperson',
            },
        ),
        migrations.CreateModel(
            name='StoreTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=200, null=True)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'db_table': 'store_transactions',
            },
        ),
        migrations.CreateModel(
            name='StoreWarehouse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=20)),
                ('store_manager', models.TextField()),
                ('salespersons', models.IntegerField()),
                ('region_ID', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='Company_income',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='business_category',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='income',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='marriage_status',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='AverageRating',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='BagType',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='BrandName',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='InventoryQuantity',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.customer'),
        ),
    ]