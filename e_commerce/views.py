from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views.generic import RedirectView, TemplateView

from .forms import LoginForm, UserForm
from .models import Comic, WishList

from django.shortcuts import render, redirect

'''Todo es parcial'''

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/e-commerce/login')
    else:
        form = UserForm()
    return render(request, 'e-commerce/register.html', {'form': form})


class LoginFormView(LoginView):
    template_name = 'e-commerce/login.html'
    
    def get_success_url(self):
        return 'purchased'


class LogoutView(RedirectView):
    pattern_name = 'login'


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
            
        
        return context
    
    
class FavoriteView(TemplateView):
    template_name = 'e-commerce/favorites.html' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.user.is_authenticated:
            user_id= self.request.user.id
            context['favoritos'] = WishList.objects.filter(user_id=user_id).count()
        
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
    
class ContacView(TemplateView):
    template_name = 'e-commerce/contacto.html'
    
class RecivedView(TemplateView):
    template_name = 'e-commerce/mail.html'