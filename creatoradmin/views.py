
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
from service.models import Service, Image_service


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



#
# ──────────────────────────────────────────────────────────────────  ──────────
#   :::::: C A T E G O R Y   R O O M : :  :   :    :     :        :          :
# ────────────────────────────────────────────────────────────────────────────
#

def categories(request):
    categories = Category.objects.all()

    context = {
        'categories':categories
    }
    return render(request, 'category_room/categories.html', context)


def category_create(request):
    if request.method == 'POST':
        form = CreateCategoryRoom(request.POST, request.FILES)
        if form.is_valid():
            category = Category()
            category.title = form.cleaned_data.get('title')
            category.description = form.cleaned_data.get('description')
            if request.FILES:
                category.image = request.FILES['image']
            category.status = form.cleaned_data.get('status')
            category.save()
            return redirect('categories')
    form = CreateCategoryRoom()
    context = {
        'form': form,
    }
    return render(request, 'category_room/category_create.html', context)


def category_edit(request, id):
    category = Category.objects.get(pk=id)
    if request.method == 'POST':
        form = EditCategoryRoom(request.POST, request.FILES, instance=category)
        if request.FILES:
            category.image = request.FILES['image']
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = EditCategoryRoom(instance=category)
        context = {'form': form,}

        return render(request, 'category_room/category_edit.html', context)


def category_delate(request, id):
    category = Category.objects.get(pk=id)
    category.delete()
    return redirect('categories')



#
# ────────────────────────────────────────────────────────────────── I ──────────
#   :::::: C A T E G O R Y   B L O G : :  :   :    :     :        :          :
# ────────────────────────────────────────────────────────────────────────────
#
def categories_blog(request):
    categories_blog = Category_Blog.objects.all()

    context = {
        'categories_blog':categories_blog
    }
    return render(request, 'category_blog/categories_blog.html', context)


def category_blog_create(request):
    if request.method == 'POST':
        form = CreateCategoryBlog(request.POST)
        if form.is_valid():
            category_blog = Category_Blog()
            category_blog.title = form.cleaned_data.get('title')
            category_blog.save()
            return redirect('categories_blog')
    form = CreateCategoryBlog()
    context = {
        'form': form,
    }
    return render(request, 'category_blog/category_blog_create.html', context)


def category_blog_edit(request, id):
    category_blog = Category_Blog.objects.get(pk=id)
    if request.method == 'POST':
        form = EditCategoryBlog(request.POST, instance=category_blog)
        if form.is_valid():
            form.save()
            return redirect('categories_blog')
    else:
        form = EditCategoryBlog(instance=category_blog)
        context = {'form': form,}

        return render(request, 'category_blog/category_blog_edit.html', context)


def category_blog_delate(request, id):
    category_blog = Category_Blog.objects.get(pk=id)
    category_blog.delete()
    return redirect('categories_blog')



#
# ────────────────────────────────────────────────  ──────────
#   :::::: B L O G : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────
#


def blogs(request):
    blogs = Blog.objects.all().order_by('id')

    context = {
        'blogs': blogs,

    }

    return render(request, 'blog/blogs.html', context)


def blog_create(request):
    if request.method == 'POST':
        form = CreateBlog(request.POST, request.FILES)
        if form.is_valid():
            blog = Blog()
            blog.title = form.cleaned_data.get('title')
            blog.description = form.cleaned_data.get('description')
            blog.text = form.cleaned_data.get('text')
            blog.category = form.cleaned_data.get('category')
            if request.FILES:
                blog.image = request.FILES['image']
            blog.status = form.cleaned_data.get('status')
            blog.save()
            return redirect('blogs')
    form = CreateBlog()
    context = {
        'form': form,
    }
    return render(request, 'blog/blog_create.html', context)


def blog_edit(request, id):
    blog = Blog.objects.get(pk=id)
    if request.method == 'POST':
        form = EditBlog(request.POST, request.FILES, instance=blog)
        if request.FILES:
            blog.image = request.FILES['image']
        if form.is_valid():
            form.save()
            return redirect('blogs')
    else:
        form = EditBlog(instance=blog)
        context = {'form': form }

        return render(request, 'blog/blog_edit.html', context)


def blog_delate(request, id):
    blog = Blog.objects.get(pk=id)
    blog.delete()
    return redirect('blogs')



#
# ────────────────────────────────────────────────────────  ──────────
#   :::::: S E R V I C E S : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────────────
#


def services(request):
    services = Service.objects.all().order_by('id')

    context = {
        'services': services,

    }

    return render(request, 'service/services.html', context)


def service_create(request):
    services = Service()
    RoomInlineFormSet = inlineformset_factory(Service, Image_service, form=CreateService, fields=('image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = CreateService(request.POST, request.FILES, instance=services, prefix='service')
        formset = RoomInlineFormSet(request.POST, request.FILES, instance=services, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            return redirect('services_admin')

    else:
        form = CreateService(instance=services, prefix='service')
        formset = RoomInlineFormSet(instance=services, prefix='images')
        
    context = {
        'form': form,
        'formset':formset,
    }
    return render(request, 'service/service_create.html', context)


def service_edit(request, id):
    service = Service.objects.get(pk=id)
    RoomInlineFormSet = inlineformset_factory(Service, Image_service, form=EditService, fields=('image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = EditService(request.POST, request.FILES, instance=service, prefix='service')
        formset = RoomInlineFormSet(request.POST, request.FILES, instance=service, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            return redirect('services_admin')

    else:
        form = EditService(instance=service, prefix='service')
        formset = RoomInlineFormSet(instance=service, prefix='images')
        
    context = {
        'form': form,
        'formset':formset,
    }
    return render(request, 'service/service_edit.html', context)


def service_delate(request, id):
    service = Service.objects.get(pk=id)
    service.delete()
    return redirect('services_admin')


#
# ────────────────────────────────────────────────────────  ──────────
#   :::::: A B O U T   U S : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────────────
#

