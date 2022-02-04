from django.shortcuts import render, redirect
from django.contrib import messages


from home.forms import *
from home.models import *
from room.models import *
from blog.models import *
from service.models import *


def home(request):
    info = Informations.objects.all().order_by('?')[:1]
    our_staff = Our_Staff.objects.all().order_by('?')[:8]
    slider = Slider.objects.all().order_by('id')
    aboutus = AboutUs.objects.all().order_by('?')[:1]
    room_picked = Room.objects.all().order_by('?')[:3]
    room_services = RoomServices.objects.all()
    services = Service.objects.all()
    gallery = Gallery.objects.all().order_by('?')[:10]
    restaurant_menu = Restaurant_menu.objects.all().order_by('?')[:2]
    special_offer = Special_offer.objects.all().order_by('?')[:3]
    blogs = Blog.objects.all().order_by('?')[:3]
    room_forms = Room.objects.values_list('title', flat=True).distinct()
    testimonials = Testimonial.objects.all()
    if request.method == 'POST':
        form = HomeOrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.name = form.cleaned_data['name']
            data.phone = form.cleaned_data['phone']
            data.guest = form.cleaned_data['guest']
            data.children = form.cleaned_data['guest']
            data.arrival = form.cleaned_data['arrival']
            data.room = form.cleaned_data['room']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(
                request, "Siz xonani bro'n qildiz aperato'r siz bilan bog'lanadi")
            return redirect('home')
    form = HomeOrderForm
    context = {
        'info': info,
        'slider': slider,
        'aboutus': aboutus,
        'room_picked': room_picked,
        'services': services,
        'gallery': gallery,
        'restaurant_menu': restaurant_menu,
        'special_offer': special_offer,
        'blogs': blogs,
        'our_staff': our_staff,
        'room_services': room_services,
        'form': form,
        'room_forms': room_forms,
        'testimonials': testimonials



    }
    return render(request, 'index.html', context)


def aboutus(request):
    aboutus = AboutUs.objects.all().order_by('?')[:1]
    licenses = License.objects.all()
    lic_images = LicImages.objects.all()
    recommended_company = Recommended_company.objects.all()
    aboutus_features = AboutUs_features.objects.all()
    image_aboutus = Image_aboutus.objects.all()
    license = License.objects.all()

    context = {
        'aboutus': aboutus,
        'licenses': licenses,
        'lic_images': lic_images,
        'recommended_company': recommended_company,
        'aboutus_features': aboutus_features,
        'image_aboutus': image_aboutus,
        'license': license

    }
    return render(request, 'about-us.html', context)


def contactus(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.phone = form.cleaned_data['phone']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Sizning xabaringiz yuborildi! Rahmat")
            return redirect('home')
    form = ContactMessageForm
    context = {'form': form, }
    return render(request, 'contact.html', context)
