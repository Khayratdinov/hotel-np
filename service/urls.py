from django.urls import path
from service import views


urlpatterns = [
    path('gallery/', views.gallery,name='gallery'),

    path('places/', views.places,name='places'),
    path('places/<int:id>/', views.place_detail,name='place-detail'),

    path('special-offers/', views.special_offers, name='special_offers'),
    path('offer-detail/<int:id>/', views.offer_detail, name='offer_detail'),

    
    path('our-staff/', views.our_staff, name='our_staff'),

    path('events/', views.events, name='events'),
    path('event_detail/<int:id>/', views.event_detail, name='event_detail'),

    path('services/', views.services, name='services'),
    path('service-detail/<int:id>/', views.service_detail, name='service_detail'),

]