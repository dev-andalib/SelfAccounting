# Generated by Django 5.1.6 on 2025-02-21 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('accountant', 'Accountant'), ('admin', 'Admin')], default='accountant', max_length=50),
        ),
    ]
