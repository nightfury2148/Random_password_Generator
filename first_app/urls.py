from django.urls import path
from . import views
  
    
  
urlpatterns = [
    path('', views.hello, name='home'),
    path('Generated_password',views.get_pass, name='password'),
    path('AboutUs',views.aboutus, name ='aboutus')
    
]