from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import routers, serializers, viewsets
from alpha_vantage.timeseries import TimeSeries
from datetime import date


# Create your views here.

# class HomePageView(TemplateView):
#     template_name = 'home.html'

# def getStock(request):
#     name = request.GET['']
#     return render(request,)

# class StockList(TemplateView):
#     def get(self, request):
#         API_key = '321CW7LWHUMB23IQ'
#         stock = 'TSLA'
#         ts = TimeSeries(key = API_key,output_format='json')
#         tsla, data = ts.get_daily_adjusted(stock)
#         return render(tsla['2021-02-08'])

class StockList(APIView):

    def get(self, request):

        tickers = ['TSLA', 'APPL', 'PLTR', 'NIO']
        arr = []


        today = str(date.today())
        API_key = '321CW7LWHUMB23IQ'
        stock = 'TSLA'        
        ts = TimeSeries(key = API_key,output_format='json')
        tsla, data = ts.get_daily_adjusted(stock)
        return Response(tsla['2021-03-05'])
        # for i in tickers:
        #     stock, data = ts.get_daily_adjusted(i)
        #     arr.append(stock)

        
        # for d in arr:
        #     return Response(d['2021-03-05'])

    

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")