from django.urls import path
from home import views


urlpatterns = [
    path('', views.home,name='home'),

    path('contactus/',views.contactus, name='contactus'),
    path('aboutus/', views.aboutus,name='aboutus'),
    
]