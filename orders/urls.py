from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.PayView.as_view(), name='pay'),
    path('closeorder/', views.CloseOrderView.as_view(), name='close'),
    path('detail/', views.DetailView.as_view(), name='detail'),
]
