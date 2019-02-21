from django.conf.urls import url
from django.views.generic import TemplateView
from myapp.views import submission

urlpatterns = [
   url(r'^submission/', submission, name='submission' )
   ]
