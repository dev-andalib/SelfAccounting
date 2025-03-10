# Generated by Django 5.1.6 on 2025-02-21 05:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('type', models.CharField(choices=[('Dividends', 'Dividends'), ('Assets', 'Assets'), ('Expenses', 'Expenses'), ('Liabilities', 'Liabilities'), ("Owner's Equity", "Owner's Equity"), ('Revenue', 'Revenue')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('client', models.CharField(max_length=255)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('added_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('debit_or_credit', models.CharField(choices=[('debit', 'Debit'), ('credit', 'Credit')], max_length=6)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('account_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='transactions', to='account.accounttype')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactions', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='account.project')),
            ],
        ),
    ]
