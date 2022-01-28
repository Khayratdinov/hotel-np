
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from creatoradmin.forms import RegisterForm

from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from room.models import Room, RoomServices, Room_Image
from home.models import Slider
from creatoradmin.forms import *


def login_form(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.warning(request, 'Error Try Again Later')
            return redirect('login_form')


    return render(request, 'profile/login.html')



def register_user(request):
    success = False

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            user.save()
            messages.success(request, 'User created - please <a href="/login">login</a>.')
            success = True

            return redirect("login_form")

        else:
           messages.warning(request, "Registration error!")
           return HttpResponseRedirect('/')
    else:
        form = RegisterForm()

    context = {
        'form':form,
        'success':success
    }

    return render(request, "profile/signup_form.html", context)


class HomeAminView(LoginRequiredMixin, TemplateView):
    template_name = "index2.html"


#======================= - ROOM CATEGORY ======================================================



#======================= - ROOM  ======================================================


def room(request):
    rooms = Room.objects.all()


    context = {
        'rooms':rooms
    }
    return render(request, 'room/room.html', context)



def room_create(request):
    room_forms = Room()
    RoomInlineFormSet = inlineformset_factory(Room, Room_Image, form=AddRoomSliderForm, fields=('room','image',), extra=5, can_delete=False, min_num=1, validate_min=True)
    RoomServiceFormSet = inlineformset_factory(Room, RoomServices, form=AddRoomServiceForm, fields=('title','description','icon',), extra=2, can_delete=False, min_num=1, validate_min=True)
    if request.method == 'POST':
        form = AddRoomForm(request.POST, request.FILES, instance=room_forms, prefix='room')
        formset = RoomInlineFormSet(request.POST, request.FILES, instance=room_forms, prefix='images')
        formset2 = RoomServiceFormSet(request.POST, instance=room_forms, prefix='services')
        if all([form.is_valid(), formset.is_valid(), formset2.is_valid(),],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            formset2.save()
            return redirect('rooms')

    else:
        form = AddRoomForm(instance=room_forms, prefix='room')
        formset = RoomInlineFormSet(instance=room_forms, prefix='images')
        formset2 = RoomServiceFormSet(instance=room_forms, prefix='services')
        
    context = {
        'form': form,
        'formset':formset,
        'formset2':formset2
    }
    return render(request, 'room/room_create.html', context)


def room_edit(request, id):
    room = Room.objects.get(pk=id)
    RoomInlineFormSet = inlineformset_factory(Room, Room_Image, form=EditRoomSliderForm, fields=('room','image',), extra=5, can_delete=True, min_num=1, validate_min=True)
    RoomServiceFormSet = inlineformset_factory(Room, RoomServices, form=EditRoomServiceForm, fields=('title','description','icon',), extra=2, can_delete=False, min_num=1, validate_min=True)
    if request.method == 'POST':
        
        form = AddRoomForm(request.POST, request.FILES, instance=room, prefix='room')
        formset = RoomInlineFormSet(request.POST, request.FILES, instance=room, prefix='images')
        formset2 = RoomServiceFormSet(request.POST, instance=room, prefix='services')

            
        if all([form.is_valid(), formset.is_valid(), formset2.is_valid(),],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            formset2.save()
            return redirect('rooms')

    else:
        form = AddRoomForm(instance=room, prefix='room')
        formset = RoomInlineFormSet(instance=room, prefix='images')
        formset2 = RoomServiceFormSet(instance=room, prefix='services')
        
    context = {
        'form': form,
        'formset':formset,
        'formset2':formset2
    }

    return render(request, 'room/room_edit.html', context)


def room_delate(request, id):
    room = Room.objects.get(pk=id)
    room.delete()
    return redirect('rooms')


#======================= - SLIDER BO'LIMI ======================================================




def sliders(request):
    sliders = Slider.objects.all()

    context = {
        'sliders':sliders
    }
    return render(request, 'slider/sliders.html', context)


def slider_create(request):
    if request.method == 'POST':
        form = CreateSlider(request.POST, request.FILES)
        if form.is_valid():
            slider = Slider()
            slider.title = form.cleaned_data.get('title')
            slider.description = form.cleaned_data.get('description')
            if request.FILES:
                slider.image = request.FILES['image']
            slider.save()
            return redirect('sliders')
    form = CreateSlider()
    context = {
        'form': form,
    }
    return render(request, 'slider/slider_create.html', context)


def slider_edit(request, id):
    slider = Slider.objects.get(pk=id)
    if request.method == 'POST':
        form = EditSlider(request.POST, request.FILES, instance=slider)
        if request.FILES:
            slider.image = request.FILES['image']
        if form.is_valid():
            form.save()
            return redirect('sliders')
    else:
        form = EditSlider(instance=slider)
        context = {'form': form,}

        return render(request, 'slider/slider_edit.html', context)


def slider_delate(request, id):
    slider = Slider.objects.get(pk=id)
    slider.delete()
    return redirect('sliders')



