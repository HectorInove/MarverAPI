from django.urls import path
from . views import *


urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('purchased', PurchaseView.as_view(), name='purchased'),
    path('table', TableView.as_view(), name='table'),
    path('cart', CartView.as_view(), name='cart'),
    path('favorites', FavoriteView.as_view(), name='favorites'),
    path('user-data', UserDataView.as_view(), name='user-data'),
    path('saludo', SaludoView.as_view(), name='saludo'),
    
    
]