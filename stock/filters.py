from django.contrib.auth.models import User
from .models import *
import django_filters

class StockFilter(django_filters.FilterSet):
	company_name = django_filters.CharFilter(lookup_expr='icontains')


	class Meta:
		model = Stock
		fields = ['company_name', ]


      