from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    client = models.CharField(max_length=255)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True, default=None)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null= True, related_name="projects")

    def __str__(self):
        return self.name



class AccountType(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ('Dividends', 'Dividends'),
        ('Assets', 'Assets'),
        ('Expenses', 'Expenses'),
        ('Liabilities', 'Liabilities'),
        ("Owner's Equity", "Owner's Equity"),
        ('Revenue', 'Revenue'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=50, choices=ACCOUNT_TYPE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.type})"





class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('debit', 'Debit'),
        ('credit', 'Credit'),
    ]

    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="transactions")
    account_type = models.ForeignKey(AccountType, on_delete=models.RESTRICT, related_name="transactions")
    debit_or_credit = models.CharField(max_length=6, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="transactions")

    def __str__(self):
        return f"{self.debit_or_credit.capitalize()} - {self.account_type.name}: {self.amount}"

