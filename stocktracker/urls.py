from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path(r'^stocks/', views.StockList.as_view()),
    path('', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
