from django.urls import path
from . views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('register', register, name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('purchased', login_required(PurchaseView.as_view()), name='purchased'),
    path('table', login_required(TableView.as_view()), name='table'),
    path('cart', login_required(CartView.as_view()), name='cart'),
    path('favorites', login_required(FavoriteView.as_view()), name='favorites'),
    path('user-data', login_required(UserDataView.as_view()), name='user-data'),
    path('saludo', SaludoView.as_view(), name='saludo'),
    path('contacto', ContacView.as_view(), name='contacto'),
    path('mail', RecivedView.as_view(), name='mail'),
    path('user-update', update, name='user-update'),
    path('pass-update', passupdate, name='pass-update'),
    path('galeria', GaleriaView.as_view(), name='galeria'), 
    
    
]