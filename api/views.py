from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import routers, serializers, viewsets, status
from rest_framework.decorators import action
from alpha_vantage.timeseries import TimeSeries
from datetime import date
import yfinance as yf
from .serializers import StockSerializer
from .models import Stock


class StockData(APIView):
    def get(self, request):
        queryset = Stock.objects.all()
        return Response('queryset')
    
    @action(detail=True, methods=['POST'])
    def post(self, request):
        # try:
            name = request.data['name']
            price = request.data['price']
            noshares = request.data['noshares']
            res = Stock.objects.create(name=name, price=price, noshares=noshares)
            serializer = StockSerializer(res, many=False)
            response = {'message:' : 'Stock added succesfully', 'result': serializer.data}
            return Response(response, status=status.HTTP_200_OK)
        # except:
            # response = {'message:' : 'Something went wrong'}
            # return Response(response, status=status.HTTP_400_BAD_REQUEST)
            # return Response(response)
            

class StockViewSet(viewsets.ModelViewSet):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()

# class StockList(TemplateView):
#     def get(self, request):
#         API_key = '321CW7LWHUMB23IQ'
#         stock = 'TSLA'
#         ts = TimeSeries(key = API_key,output_format='json')
#         tsla, data = ts.get_daily_adjusted(stock)
#         return render(tsla['2021-02-08'])

class StockNameViewSet(viewsets.ModelViewSet):
    serializer_class = StockSerializer
    queryset = Stock.objects.only('name')

class StockList(APIView):

    def get(self, request):
        symbols = []
        dict = {}
        queryset = Stock.objects.all()
        for query in queryset:
            symbols.append(query.name)
        tickers = yf.Tickers(symbols)
        for s in symbols:
            dict[s] = tickers.tickers[s].info['regularMarketPrice']
        return Response(dict)
            