from django.urls import path
from . views import *


urlpatterns = [
    path('purchased', PurchaseView.as_view(), name='purchased'),
    path('form', FormView.as_view(), name='form'),
    path('table', TableView.as_view(), name='table'),
    path('cart', CartView.as_view(), name='cart'),
    path('favorites', FavoriteView.as_view(), name='favorites'),
    path('edit', EditView.as_view(), name='edit'),
    
    
]