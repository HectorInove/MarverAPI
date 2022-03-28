from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views.generic import RedirectView, TemplateView

from .forms import LoginForm
from .models import Comic

'''Todo es parcial'''

class LoginFormView(LoginView):
    template_name = 'e-commerce/login.html'
    
    def get_success_url(self):
        return 'purchased'


class LogoutView(RedirectView):
    pattern_name = 'login'


class PurchaseView(TemplateView):
    template_name = 'e-commerce/purchased.html'
   
   
class FormView(TemplateView):
    template_name = 'e-commerce/form.html'
    
    
class TableView(TemplateView):
    template_name = 'e-commerce/tabla.html'
    

class CartView(TemplateView):
    template_name = 'e-commerce/cart.html'
    
    
class FavoriteView(TemplateView):
    template_name = 'e-commerce/favorites.html'
    
class EditView(TemplateView):
    template_name = 'e-commerce/edit.html'  


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
    
    