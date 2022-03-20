from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ListProductsListView.as_view(), name="list"),
    path('<slug>', views.DetailProductsView.as_view(), name="detail"),
    path('addcart/', views.AddCartView.as_view(), name="addcart"),
    path('removecart/', views.RemoveCartView.as_view(), name="removecart"),
    path('cart/', views.CartView.as_view(), name="cart"),
    path('conclude/', views.ConcludeView.as_view(), name="conclude"),
]
