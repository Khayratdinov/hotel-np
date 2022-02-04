from django.urls import path
from service import views


urlpatterns = [

    # ---------------------------------------------------------------------------- #
    
    path('gallery/', views.gallery,name='gallery'),

    # ---------------------------------------------------------------------------- #

    path('places/', views.places,name='places'),
    path('places/<int:id>/', views.place_detail,name='place-detail'),

    # ---------------------------------------------------------------------------- #

    path('special-offers/', views.special_offers, name='special_offers'),
    path('special_offer_detail/<int:id>/', views.special_offer_detail, name='special_offer_detail'),

    # ---------------------------------------------------------------------------- #

    path('our-staff/', views.our_staff, name='our_staff'),

    # ---------------------------------------------------------------------------- #

    path('events/', views.events, name='events'),
    path('event_detail/<int:id>/', views.event_detail, name='event_detail'),
    
    # ---------------------------------------------------------------------------- #

    path('services/', views.services, name='services'),
    path('service_detail/<int:id>/', views.service_detail, name='service_detail'),

    # ---------------------------------------------------------------------------- #

    path('business_detail/<int:id>/', views.business_detail, name='business_detail'),

    # ---------------------------------------------------------------------------- #

    path('restaurant_detail/<int:id>/', views.restaurant_detail, name='restaurant_detail'),

    # ---------------------------------------------------------------------------- #

    path('spa_detail/<int:id>/', views.spa_detail, name='spa_detail'),

    # ---------------------------------------------------------------------------- #

    path('fitness_detail/<int:id>/', views.fitness_detail, name='fitness_detail'),



]