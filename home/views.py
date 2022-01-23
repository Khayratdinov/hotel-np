from django.shortcuts import render, redirect
from django.core.paginator import (Paginator, PageNotAnInteger, EmptyPage)
from django.contrib import messages
from django.utils import translation
from django.http import HttpResponseRedirect

from home.forms import OrderForm, ContactForm

from room.models import Room
from blog.models import Blog
from home.models import Informations, License, LicImages, ContactMessage, FAQ, AboutUs, Slider
from service.models import (Service, Special_offer, Offer_order, Gallery,
                            Our_Staff, Restaurant_menu,
                            Events, Place,
                            )



def home(request):
    info = Informations.objects.all()
    our_staff = Our_Staff.objects.all().order_by('?')[:8]
    slider = Slider.objects.all().order_by('id')
    aboutus = AboutUs.objects.all()
    room_picked = Room.objects.all().order_by('?')[:3]
    services = Service.objects.all()
    gallery = Gallery.objects.all().order_by('?')[:10]
    restaurant_menu = Restaurant_menu.objects.all().order_by('?')[:2]
    special_offer = Special_offer.objects.all().order_by('?')[:3]
    blogs = Blog.objects.all().order_by('?')[:3]
    context = {
        'info': info,
        'slider':slider,
        'aboutus' : aboutus,
        'room_picked': room_picked,
        'services' : services,
        'gallery' : gallery,
        'restaurant_menu' : restaurant_menu,
        'special_offer' : special_offer,
        'blogs' : blogs,
        'our_staff': our_staff,

        
    }
    return render(request, 'index.html', context)





def aboutus(request):
    aboutus = AboutUs.objects.all().order_by('id')
    licenses = License.objects.all()
    lic_images  = LicImages.objects.all()

    context = {
        'aboutus': aboutus,
        'licenses': licenses,
        'lic_images': lic_images,

    }
    return render(request, 'about-us.html', context)


def contactus(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
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
    form = ContactForm
    context = {'form': form,}
    return render(request,'contact.html', context)




