from django.views.generic import TemplateView
from . models import Comic


'''Todo es parcial'''
  
class IndexView(TemplateView):
    template_name = 'e-commerce/index.html'
    #retorna tabla con comics disponibles
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['comic'] = Comic.objects.all()
        return context
   
  
        
        
    
    