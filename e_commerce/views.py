from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import RedirectView, TemplateView

from .forms import LoginForm, UserForm, UserUpdateForm
from .models import Comic, WishList
from datetime import datetime

from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

'''Todo es parcial'''
#Registro de usuario
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/e-commerce/login')
    else:
        form = UserForm()
    return render(request, 'e-commerce/register.html', {'form': form})

#Edicion de perfil d eusuario
def update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user-data')
    else:
        form = UserUpdateForm(instance=request.user)
        return render(request, 'e-commerce/userupdate.html', {'form': form})

#Edicion de password de usuario     
def passupdate(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'e-commerce/userchangepass.html', {'form': form})  

class LoginFormView(LoginView):
    template_name = 'e-commerce/login.html'
    
    def get_success_url(self):
        return 'purchased'


class LogoutView(RedirectView):
    pattern_name = 'login'
    
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)


class PurchaseView(TemplateView):
    template_name = 'e-commerce/purchased.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comic'] = Comic.objects.all()
        
        return context
    
    
class TableView(TemplateView):
    template_name = 'e-commerce/tabla.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comic'] = Comic.objects.all()
        return context
    

class CartView(TemplateView):
    template_name = 'e-commerce/cart.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.user.is_authenticated:
            user_id= self.request.user.id
            context['cart'] = WishList.objects.filter(user_id=user_id, cart=True).count()
            data = WishList.objects.filter(user_id=user_id, cart=True)
            id= [id[0] for id in data.values_list()]
            comic = Comic.objects.filter(id__in=id)
            context['comic'] = comic.values()
            id= [id.comic_id for id in data]
            context['total_price'] = round((sum([float(comic.price) for comic in id])), 2)
        
        return context
    
    
class FavoriteView(TemplateView):
    template_name = 'e-commerce/favorites.html' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.user.is_authenticated:
            user_id= self.request.user.id
            context['favoritos'] = WishList.objects.filter(user_id=user_id).count()
            
            data = WishList.objects.filter(user_id=user_id, favorite=True)
            id= [id[0] for id in data.values_list()]
            comic = Comic.objects.filter(id__in=id)
            context['comic'] = comic.values()
        return context


class UserDataView(TemplateView):
    template_name = 'e-commerce/user.html' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            id_user = self.request.user.pk 
            queryset = User.objects.filter(id=id_user)
            user_data = queryset.values().first()
            context['user_data'] = user_data
        
        return context    
    
class SaludoView(TemplateView):
    template_name = 'e-commerce/saludo.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        user = User.objects.get(username=self.request.user)
        data = WishList.objects.filter(user_id=user, cart=True, wished_qty__gt=0)
        comics = [obj.comic_id for obj in data]
        context['comics'] = comics
        
        if data:
            time = datetime.now()
            context['date'] = time.strftime('%Y-%m-%d')
            
        for (comic, wish_obj) in zip(comics, data):
            comic.stock_qty = comic.stock_qty - wish_obj.wished_qty
            comic.save()
            wish_obj.buied_qty += wish_obj.wished_qty
            wish_obj.wished_qty = 0
            wish_obj.cart = False
            wish_obj.save()
            
        return context
    
class ContacView(TemplateView):
    template_name = 'e-commerce/contacto.html'
    
class RecivedView(TemplateView):
    template_name = 'e-commerce/mail.html'
    
class GaleriaView(TemplateView):
    template_name = 'e-commerce/galeria.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comic'] = Comic.objects.all()
        return context