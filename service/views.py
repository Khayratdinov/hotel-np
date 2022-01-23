from django.http import request
from django.shortcuts import render
from service.models import (
                            Gallery, Category_gallery, Place, Image_place,
                            Service, Image_service, Special_offer, Image_offer,
                            Offer_order, Our_Staff, Events, Image_events, Category_staff
                            )
# Create your views here.


def gallery(request):
    gallerys = Gallery.objects.all()
    categories_gallery = Category_gallery.objects.all()
    context = {
        'gallerys': gallerys,
        'categories_gallery': categories_gallery,
     }
    return render(request, 'service/gallery.html', context)


def special_offers(request):
    special_offers = Special_offer.objects.all()
    context = {
        'special_offers': special_offers,
    }
    return render(request, 'service/special_offers.html', context)

def offer_detail(request, id):
    special_offer = Special_offer.objects.get(pk=id)
    image_offer = Image_offer.objects.filter(special_offer_id=id)


    context = {
        'special_offer': special_offer,
        'image_offer' : image_offer,
    }
    return render(request, 'service/offer-detail.html', context)


def our_staff(request):
    our_staff = Our_Staff.objects.all()

    context = {
        'our_staff': our_staff
    }
    return render(request, 'service/our-staff.html', context)

def events(request):
    events = Events.objects.all()

    context = {
        'events': events
    }
    return render(request, 'service/events.html', context)

def event_detail(request, id):
    events = Events.objects.get(pk=id)
    image_events = Image_events.objects.filter(events_id=id)
    context = {
        'events': events,
        'image_events': image_events,
    }
    return render(request, 'service/event-detail.html', context)



def places(request):
    places = Place.objects.all()
    context = {
        'places':places,
    }
    return render(request, 'service/places.html', context)

def place_detail(request, id):
    place = Place.objects.get(pk=id)
    place_images = Image_place.objects.filter(place_id=id)
    context = {
        'place':place,
        'place_images': place_images,
    }
    return render(request, 'service/place-details.html', context)

def services(request):
    services = Service.objects.all()
    context = {
        'services':services,
    }
    return render(request, 'service/spa.html', context)

def service_detail(request, id):
    staff = Our_Staff.objects.all()
    service = Service.objects.get(pk=id)
    image_service = Image_service.objects.filter(pk=id)
    context = {
        'service':service,
        'staff': staff,
        'image_service': image_service,
    }
    return render(request, 'service/service-detail.html', context)