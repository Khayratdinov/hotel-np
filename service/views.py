from django.shortcuts import render, redirect
from django.contrib import messages


from service.models import *
from home.forms import *

# Create your views here.


# ---------------------------------------------------------------------------- #
#                                   HOME PAGE                                  #
# ---------------------------------------------------------------------------- #


# ────────────────────────── SPECIAL OFFER FRONT END ───────────────────────── #


def special_offers(request):
    special_offers = Special_offer.objects.all()
    context = {
        'special_offers': special_offers,
    }
    return render(request, 'service/special_offers.html', context)


def special_offer_detail(request, id):
    special_offer = Special_offer.objects.get(pk=id)
    image_offer = Image_offer.objects.filter(special_offer_id=id)

    if request.method == 'POST':
        form = SpecialOfferForm(request.POST, instance=special_offer)
        if form.is_valid():
            data = Offer_order()
            data.offer_id = special_offer.id
            data.name = form.cleaned_data['name']
            data.phone = form.cleaned_data['phone']
            data.date = form.cleaned_data['date']
            data.text = form.cleaned_data['text']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "sorovingiz qabul qilindi")
            return redirect('home')
    form = SpecialOfferForm(instance=special_offer)

    context = {
        'special_offer': special_offer,
        'image_offer': image_offer,
        'form': form,
    }
    return render(request, 'service/special_offer_detail.html', context)


# ───────────────────────────── EVENTS FRONT END ───────────────────────────── #


def events(request):
    events = Events.objects.all()

    context = {
        'events': events
    }
    return render(request, 'service/events.html', context)


def event_detail(request, id):
    events = Events.objects.get(pk=id)
    image_events = Image_events.objects.filter(events_id=id)

    if request.method == 'POST':
        form = EventsOrderForm(request.POST, instance=events)
        if form.is_valid():
            data = Offer_events_ticket()
            data.offer_id = events.id
            data.name = form.cleaned_data['name']
            data.phone = form.cleaned_data['phone']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "sorovingiz qabul qilindi")
            return redirect('home')
    form = EventsOrderForm(instance=events)
    context = {
        'events': events,
        'image_events': image_events,
        'form': form
    }
    return render(request, 'service/event_detail.html', context)


# ────────────────────────────── PLACE FRONT END ───────────────────────────── #


def places(request):
    places = Place.objects.all()
    context = {
        'places': places,
    }
    return render(request, 'service/places.html', context)


def place_detail(request, id):
    place = Place.objects.get(pk=id)
    place_images = Image_place.objects.filter(place_id=id)
    context = {
        'place': place,
        'place_images': place_images,
    }
    return render(request, 'service/place_detail.html', context)


# ──────────────────────────── SERVICES FRONT END ──────────────────────────── #


def services(request):
    services = Service.objects.all()
    context = {
        'services': services,
    }
    return render(request, 'service/spa.html', context)


def service_detail(request, id):

    staff = Our_Staff.objects.all()
    service = Service.objects.get(id=id)
    image_service = Image_service.objects.filter(service_id=id)
    context = {
        'service': service,
        'staff': staff,
        'image_service': image_service,
    }
    return render(request, 'service/service_detail.html', context)


# ---------------------------------------------------------------------------- #


def business_detail(request, id):
    business = Business.objects.get(id=id)
    image_business = Image_business.objects.filter(business_id=id)
    context = {
        'business': business,
        'image_business': image_business,
    }
    return render(request, 'service/business_detail.html', context)


# ---------------------------------------------------------------------------- #


def restaurant_detail(request, id):
    restaurant = Restaurant.objects.get(id=id)
    image_restaurant = Image_restaurant.objects.filter(restaurant_id=id)
    context = {
        'restaurant': restaurant,
        'image_restaurant': image_restaurant,
    }
    return render(request, 'service/restaurant_detail.html', context)


# ---------------------------------------------------------------------------- #


def spa_detail(request, id):
    spa = Spa.objects.get(id=id)
    image_spa = Image_spa.objects.filter(spa_id=id)
    context = {
        'spa': spa,
        'image_spa': image_spa,
    }
    return render(request, 'service/spa_detail.html', context)


# ---------------------------------------------------------------------------- #


def fitness_detail(request, id):
    fitness = Fitness.objects.get(id=id)
    image_fitness = Image_fitness.objects.filter(fitness_id=id)
    context = {
        'fitness': fitness,
        'image_fitness': image_fitness,
    }
    return render(request, 'service/fitness_detail.html', context)


# ---------------------------------------------------------------------------- #


def our_staff(request):
    our_staff = Our_Staff.objects.all()

    context = {
        'our_staff': our_staff
    }
    return render(request, 'service/our_staff.html', context)


# ---------------------------------------------------------------------------- #


def gallery(request):
    gallerys = Gallery.objects.all()
    categories_gallery = Category_gallery.objects.all()
    context = {
        'gallerys': gallerys,
        'categories_gallery': categories_gallery,
    }
    return render(request, 'service/gallery.html', context)


# ---------------------------------------------------------------------------- #
