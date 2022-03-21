from django.urls import path
from . views import BaseView, IndexView


urlpatterns = [
    path('base-view', BaseView.as_view(), name='base-view'),
    path('index', IndexView.as_view(), name='index'),
]