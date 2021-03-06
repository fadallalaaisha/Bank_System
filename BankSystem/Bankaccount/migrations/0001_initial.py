# Generated by Django 3.2.5 on 2021-07-12 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.PositiveIntegerField(max_length=12)),
                ('balance_amount', models.PositiveBigIntegerField()),
                ('deposit', models.PositiveBigIntegerField()),
                ('withdraw', models.PositiveIntegerField(max_length=8)),
                ('code_number', models.CharField(max_length=5)),
                ('loan', models.CharField(max_length=6)),
                ('Repay', models.PositiveIntegerField()),
                ('Customers', models.CharField(max_length=10)),
                ('Transfer', models.PositiveIntegerField()),
            ],
        ),
    ]
