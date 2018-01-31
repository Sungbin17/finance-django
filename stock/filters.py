from django.contrib.auth.models import User
from .models import *
import django_filters

class StockFilter(django_filters.FilterSet):
    class Meta:
        model = Stock
        fields = ['company_name', ]