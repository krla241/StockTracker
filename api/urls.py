from django.urls import path, include
from . import views
from rest_framework import routers
from .views import StockViewSet
from .views import StockNameViewSet

router = routers.DefaultRouter()
router.register('sets', StockViewSet)
router.register('allnames', StockNameViewSet)

urlpatterns = [

    path('stocks', views.StockList.as_view()),
    path('database', views.StockData.as_view()),
    path('api', include(router.urls))
]