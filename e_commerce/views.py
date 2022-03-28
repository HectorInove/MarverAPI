from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.views import LoginView, LogoutView
from . models import Comic
from . forms import LoginForm


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
    
    