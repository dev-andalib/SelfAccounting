from django.contrib import admin
from .models import Project, AccountType, Transaction


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'client', 'start_date', 'end_date', 'added_by')
    search_fields = ('name', 'client')
    list_filter = ('start_date', 'end_date')
    ordering = ('-start_date',)

@admin.register(AccountType)
class AccountTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    search_fields = ('name',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('project', 'account_type', 'debit_or_credit', 'amount', 'date_created', 'created_by')
    list_filter = ('debit_or_credit', 'date_created')
    search_fields = ('project__name', 'account_type__name', 'created_by__username')
    ordering = ('-date_created',)

