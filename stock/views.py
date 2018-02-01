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
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt

from fbprophet import Prophet
from datetime import datetime
import io
from pandas.compat import StringIO
import PIL, PIL.Image
from django.conf import settings

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



def stock_detail(request, pk):
    fig=plt.figure(figsize=(6, 4.5), dpi=80,facecolor='w', edgecolor='w')
    stock = get_object_or_404(Stock, pk=pk)
    start = datetime(1990, 1, 1)
    end = datetime(2017, 6, 30)
    print('KRX:'+stock.index1)
    STOCK = web.DataReader('KRX:'+stock.index1,'google',start,end) 
    print(STOCK.head())
    STOCK_trunc = STOCK[:'2016-12-31']
    df = pd.DataFrame({'ds':STOCK_trunc.index, 'y':STOCK_trunc['Close']})
    df.reset_index(inplace=True)
    del df['Date']
    m = Prophet(daily_seasonality=True)
    m.fit(df);
    future = m.make_future_dataframe(periods=365)
    forecast = m.predict(future)
    m.plot(forecast)
    plt.savefig('1.png')








    ctx = {
        'stock': stock,
        'forecast':forecast,
        'm':m,
        'df':df,
        'name':stock.company_name

    }
    return render(request, 'stock/stock_detail.html', ctx)


















