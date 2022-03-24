from django.views.generic import TemplateView
from . models import Comic


'''Todo es parcial'''

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
        
    
    