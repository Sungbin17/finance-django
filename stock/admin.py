from django.contrib import admin

from .models import *

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
	list_display = ('company_name', 'index1', 'sector', 'major_product')
	search_fields = ['company_name']