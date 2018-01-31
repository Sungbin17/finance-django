from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.urls import reverse
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User

from .filters import StockFilter

def search(request):
    stock_list = Stock.objects.all()
    stock_filter = StockFilter(request.GET, queryset=stock_list)
    return render(request, 'stock/stock_list2.html', {'filter': stock_filter})

def stock_list(request):

    stock_list = Stock.objects.all()
    ctx = {
        'stock_list': stock_list,

    }
    return render(request, 'stock/stock_list.html', ctx)