from django.views.generic import TemplateView
from . models import Comic


class BaseView(TemplateView):
    template_name = 'e-commerce/base.html'
    
class IndexView(TemplateView):
    template_name = 'e-commerce/index.html'
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['comic'] = Comic.objects.all()
        return context
    
    