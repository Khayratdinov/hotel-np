
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from creatoradmin.forms import RegisterForm
from django.contrib import messages

from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from room.models import Room, RoomServices, Room_Image
from home.models import Slider, AboutUs, Image_aboutus, AboutUs_features
from creatoradmin.forms import *
from service.models import Business, Image_business, Image_events, Image_fitness, Image_offer, Image_place, Image_restaurant, Image_spa , Service, Image_service


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
        form = SliderForm(request.POST, request.FILES)
        if form.is_valid():
            slider = Slider()
            slider.title = form.cleaned_data.get('title')
            slider.description = form.cleaned_data.get('description')
            if request.FILES:
                slider.image = request.FILES['image']
            slider.save()
            return redirect('sliders')
    form = SliderForm()
    context = {
        'form': form,
    }
    return render(request, 'slider/slider_create.html', context)


def slider_edit(request, id):
    slider = Slider.objects.get(pk=id)
    if request.method == 'POST':
        form = SliderForm(request.POST, request.FILES, instance=slider)
        if request.FILES:
            slider.image = request.FILES['image']
        if form.is_valid():
            form.save()
            return redirect('sliders')
    else:
        form = SliderForm(instance=slider)
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
    RoomInlineFormSet = inlineformset_factory(Room, Room_Image, form=RoomSliderForm, fields=('room','image',), extra=5, can_delete=False, min_num=1, validate_min=True)
    RoomServiceFormSet = inlineformset_factory(Room, RoomServices, form=RoomServiceForm, fields=('title','description','icon',), extra=2, can_delete=False, min_num=1, validate_min=True)
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES, instance=room_forms, prefix='room')
        formset = RoomInlineFormSet(request.POST, request.FILES, instance=room_forms, prefix='images')
        formset2 = RoomServiceFormSet(request.POST, instance=room_forms, prefix='services')
        if all([form.is_valid(), formset.is_valid(), formset2.is_valid(),],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            formset2.save()
            return redirect('rooms_admin')

    else:
        form = RoomForm(instance=room_forms, prefix='room')
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
    RoomInlineFormSet = inlineformset_factory(Room, Room_Image, form=RoomSliderForm, fields=('room','image',), extra=5, can_delete=True, min_num=1, validate_min=True)
    RoomServiceFormSet = inlineformset_factory(Room, RoomServices, form=RoomServiceForm, fields=('title','description','icon',), extra=2, can_delete=False, min_num=1, validate_min=True)
    if request.method == 'POST':
        
        form = RoomForm(request.POST, request.FILES, instance=room, prefix='room')
        formset = RoomInlineFormSet(request.POST, request.FILES, instance=room, prefix='images')
        formset2 = RoomServiceFormSet(request.POST, instance=room, prefix='services')

            
        if all([form.is_valid(), formset.is_valid(), formset2.is_valid(),],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            formset2.save()
            return redirect('rooms_admin')

    else:
        form = RoomForm(instance=room, prefix='room')
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
    return redirect('rooms_admin')



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
        form = CategoryRoomForm(request.POST, request.FILES)
        if form.is_valid():
            category = Category()
            category.title = form.cleaned_data.get('title')
            category.description = form.cleaned_data.get('description')
            if request.FILES:
                category.image = request.FILES['image']
            category.status = form.cleaned_data.get('status')
            category.save()
            return redirect('categories')
    form = CategoryRoomForm()
    context = {
        'form': form,
    }
    return render(request, 'category_room/category_create.html', context)


def category_edit(request, id):
    category = Category.objects.get(pk=id)
    if request.method == 'POST':
        form = CategoryRoomForm(request.POST, request.FILES, instance=category)
        if request.FILES:
            category.image = request.FILES['image']
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryRoomForm(instance=category)
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
        form = CategoryBlogForm(request.POST)
        if form.is_valid():
            category_blog = Category_Blog()
            category_blog.title = form.cleaned_data.get('title')
            category_blog.save()
            return redirect('categories_blog')
    form = CategoryBlogForm()
    context = {
        'form': form,
    }
    return render(request, 'category_blog/category_blog_create.html', context)


def category_blog_edit(request, id):
    category_blog = Category_Blog.objects.get(pk=id)
    if request.method == 'POST':
        form = CategoryBlogForm(request.POST, instance=category_blog)
        if form.is_valid():
            form.save()
            return redirect('categories_blog')
    else:
        form = CategoryBlogForm(instance=category_blog)
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
        form = BlogForm(request.POST, request.FILES)
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
    form = BlogForm()
    context = {
        'form': form,
    }
    return render(request, 'blog/blog_create.html', context)


def blog_edit(request, id):
    blog = Blog.objects.get(pk=id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if request.FILES:
            blog.image = request.FILES['image']
        if form.is_valid():
            form.save()
            return redirect('blogs')
    else:
        form = BlogForm(instance=blog)
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
    RoomInlineFormSet = inlineformset_factory(Service, Image_service, form=ServiceForm, fields=('image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=services, prefix='service')
        formset = RoomInlineFormSet(request.POST, request.FILES, instance=services, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            return redirect('services_admin')

    else:
        form = ServiceForm(instance=services, prefix='service')
        formset = RoomInlineFormSet(instance=services, prefix='images')
        
    context = {
        'form': form,
        'formset':formset,
    }
    return render(request, 'service/service_create.html', context)


def service_edit(request, id):
    service = Service.objects.get(pk=id)
    RoomInlineFormSet = inlineformset_factory(Service, Image_service, form=ServiceForm, fields=('image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service, prefix='service')
        formset = RoomInlineFormSet(request.POST, request.FILES, instance=service, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            return redirect('services_admin')

    else:
        form = ServiceForm(instance=service, prefix='service')
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



def aboutus_admin(request):
    aboutus = AboutUs.objects.all().order_by('id')

    context = {
        'aboutus': aboutus,

    }

    return render(request, 'aboutus/aboutus_admin.html', context)


def aboutus_create(request):
    if request.method == 'POST':
        form = AboutUsForm(request.POST, request.FILES)
        if form.is_valid():
            aboutus = AboutUs()
            aboutus.title = form.cleaned_data.get('title')
            aboutus.description = form.cleaned_data.get('description')
            aboutus.text = form.cleaned_data.get('text')
            if request.FILES:
                aboutus.image = request.FILES['image']

            aboutus.save()
            return redirect('aboutus_admin')
    form = AboutUsForm()
    context = {
        'form': form,
    }
    return render(request, 'aboutus/aboutus_create.html', context)


def aboutus_edit(request, id):
    aboutus = AboutUs.objects.get(pk=id)
    if request.method == 'POST':
        form = AboutUsForm(request.POST, request.FILES, instance=aboutus)
        if request.FILES:
            aboutus.image = request.FILES['image']
        if form.is_valid():
            form.save()
            return redirect('aboutus_admin')
    else:
        form = AboutUsForm(instance=aboutus)
        context = {'form': form }

        return render(request, 'aboutus/aboutus_edit.html', context)


def aboutus_delate(request, id):
    aboutus = AboutUs.objects.get(pk=id)
    aboutus.delete()
    return redirect('aboutus_admin')



#
# ──────────────────────────────────────────────────────────────────────  ──────────
#   :::::: A B O U T   U S   I M A G E S : :  :   :    :     :        :          :
# ────────────────────────────────────────────────────────────────────────────────
#


def aboutus_image_admin(request):
    aboutus_images = Image_aboutus.objects.all().order_by('id')

    context = {
        'aboutus_images': aboutus_images,

    }

    return render(request, 'aboutus_image/aboutus_image_admin.html', context)


def aboutus_image_create(request):
    if request.method == 'POST':
        form = AboutUsImageForm(request.POST, request.FILES)
        if form.is_valid():
            aboutus_images = Image_aboutus()
            aboutus_images.title = form.cleaned_data.get('title')
            aboutus_images.description = form.cleaned_data.get('description')
            if request.FILES:
                aboutus_images.image = request.FILES['image']

            aboutus_images.save()
            return redirect('aboutus_image_admin')
    form = AboutUsImageForm()
    context = {
        'form': form,
    }
    return render(request, 'aboutus_image/aboutus_image_create.html', context)


def aboutus_image_edit(request, id):
    aboutus_image = Image_aboutus.objects.get(pk=id)
    if request.method == 'POST':
        form = AboutUsImageForm(request.POST, request.FILES, instance=aboutus_image)
        if request.FILES:
            aboutus_image.image = request.FILES['image']
        if form.is_valid():
            form.save()
            return redirect('aboutus_image_admin')
    else:
        form = AboutUsImageForm(instance=aboutus_image)
        context = {'form': form }

        return render(request, 'aboutus_image/aboutus_image_edit.html', context)


def aboutus_image_delate(request, id):
    aboutus_image = Image_aboutus.objects.get(pk=id)
    aboutus_image.delete()
    return redirect('aboutus_image_admin')



#
# ──────────────────────────────────────────────────────────────────────────  ──────────
#   :::::: A B O U T   U S   F E A T U R E S : :  :   :    :     :        :          :
# ────────────────────────────────────────────────────────────────────────────────────
#


def aboutus_feature_admin(request):
    aboutus_features = AboutUs_features.objects.all().order_by('id')

    context = {
        'aboutus_features': aboutus_features,

    }

    return render(request, 'aboutus_feature/aboutus_feature_admin.html', context)


def aboutus_feature_create(request):
    if request.method == 'POST':
        form = AboutUsFeatureForm(request.POST, request.FILES)
        if form.is_valid():
            aboutus_feature = AboutUs_features()
            aboutus_feature.name = form.cleaned_data.get('name')
            aboutus_feature.number = form.cleaned_data.get('number')
            aboutus_feature.icon = form.cleaned_data.get('icon')
            if request.FILES:
                aboutus_feature.image = request.FILES['image']

            aboutus_feature.save()
            return redirect('aboutus_feature_admin')
    form = AboutUsFeatureForm()
    context = {
        'form': form,
    }
    return render(request, 'aboutus_feature/aboutus_feature_create.html', context)


def aboutus_feature_edit(request, id):
    aboutus_feature = AboutUs_features.objects.get(pk=id)
    if request.method == 'POST':
        form = AboutUsFeatureForm(request.POST, request.FILES, instance=aboutus_feature)
        if request.FILES:
            aboutus_feature.image = request.FILES['image']
        if form.is_valid():
            form.save()
            return redirect('aboutus_feature_admin')
    else:
        form = AboutUsFeatureForm(instance=aboutus_feature)
        context = {'form': form }

        return render(request, 'aboutus_feature/aboutus_feature_edit.html', context)


def aboutus_feature_delate(request, id):
    aboutus_feature = AboutUs_features.objects.get(pk=id)
    aboutus_feature.delete()
    return redirect('aboutus_feature_admin')



#
# ────────────────────────────────────────────────────────  ──────────
#   :::::: B U S I N E S S : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────────────
#


def business_admin(request):
    business = Business.objects.all().order_by('id')

    context = {
        'business': business,
    }

    return render(request, 'business/business_admin.html', context)


def business_create(request):
    business = Business()
    InlineFormSet = inlineformset_factory(Business, Image_business, form=BusinessForm, fields=('image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES, instance=business, prefix='business')
        formset = InlineFormSet(request.POST, request.FILES, instance=business, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request,"Malumotlaringiz qoshildi ")
            return redirect('business_admin')

    else:
        form = BusinessForm(instance=business, prefix='business')
        formset = InlineFormSet(instance=business, prefix='images')
        
    context = {
        'form': form,
        'formset':formset,
    }
    return render(request, 'business/business_create.html', context)


def business_edit(request, id):
    business = Business.objects.get(pk=id)
    InlineFormSet = inlineformset_factory(Business, Image_business, form=BusinessForm, fields=('image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES, instance=business, prefix='business')
        formset = InlineFormSet(request.POST, request.FILES, instance=business, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request,"Malumotlaringiz o`zgartirildi")
            return redirect('business_admin')

    else:
        form = BusinessForm(instance=business, prefix='business')
        formset = InlineFormSet(instance=business, prefix='images')
        
    context = {
        'form': form,
        'formset':formset,
    }
    return render(request, 'business/business_edit.html', context)


def business_delate(request, id):
    business = Business.objects.get(pk=id)
    business.delete()
    messages.success(request,"Malumotlaringiz o'chirildi ")
    return redirect('business_admin')



#
# ────────────────────────────────────────────────────────────  ──────────
#   :::::: R E S T A U R A N T : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────────────────
#


def restaurant_admin(request):
    restaurant = Restaurant.objects.all().order_by('id')

    context = {
        'restaurant': restaurant,
    }

    return render(request, 'restaurant/restaurant_admin.html', context)


def restaurant_create(request):
    restaurant = Restaurant()
    InlineFormSet = inlineformset_factory(Restaurant, Image_restaurant, form=RestaurantForm, fields=('image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES, instance=restaurant, prefix='restaurant')
        formset = InlineFormSet(request.POST, request.FILES, instance=restaurant, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request,"Malumotlaringiz qoshildi ")
            return redirect('restaurant_admin')

    else:
        form = RestaurantForm(instance=restaurant, prefix='restaurant')
        formset = InlineFormSet(instance=restaurant, prefix='images')
        
    context = {
        'form': form,
        'formset':formset,
    }
    return render(request, 'restaurant/restaurant_create.html', context)


def restaurant_edit(request, id):
    restaurant = Restaurant.objects.get(pk=id)
    InlineFormSet = inlineformset_factory(Restaurant, Image_restaurant, form=RestaurantForm, fields=('image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES, instance=restaurant, prefix='restaurant')
        formset = InlineFormSet(request.POST, request.FILES, instance=restaurant, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request,"Malumotlaringiz o`zgartirildi")
            return redirect('restaurant_admin')

    else:
        form = RestaurantForm(instance=restaurant, prefix='restaurant')
        formset = InlineFormSet(instance=restaurant, prefix='images')
        
    context = {
        'form': form,
        'formset':formset,
    }
    return render(request, 'restaurant/restaurant_edit.html', context)


def restaurant_delate(request, id):
    restaurant = Restaurant.objects.get(pk=id)
    restaurant.delete()
    messages.success(request,"Malumotlaringiz o'chirildi ")
    return redirect('restaurant_admin')



#
# ──────────────────────────────────────────────────────────────────────  ──────────
#   :::::: R E S T A U R A N T   M E N U : :  :   :    :     :        :          :
# ────────────────────────────────────────────────────────────────────────────────
#

def restaurant_menu_admin(request):
    restaurant_menu = Restaurant_menu.objects.all().order_by('id')

    context = {
        'restaurant_menu': restaurant_menu,

    }

    return render(request, 'restaurant_menu/restaurant_menu_admin.html', context)


def restaurant_menu_create(request):
    if request.method == 'POST':
        form = RestaurantMenuForm(request.POST, request.FILES)
        if form.is_valid():
            restaurant_menu = Restaurant_menu()
            restaurant_menu.title = form.cleaned_data.get('title')
            restaurant_menu.description = form.cleaned_data.get('description')
            restaurant_menu.price = form.cleaned_data.get('price')
            
            if request.FILES:
                restaurant_menu.image = request.FILES['image']

            restaurant_menu.status = form.cleaned_data.get('status')

            restaurant_menu.save()
            messages.success(request,"Malumotlaringiz qoshildi ")
            return redirect('restaurant_menu_admin')
    form = RestaurantMenuForm()
    context = {
        'form': form,
    }
    return render(request, 'restaurant_menu/restaurant_menu_create.html', context)


def restaurant_menu_edit(request, id):
    restaurant_menu = Restaurant_menu.objects.get(pk=id)
    if request.method == 'POST':
        form = RestaurantMenuForm(request.POST, request.FILES, instance=restaurant_menu)
        if request.FILES:
            restaurant_menu.image = request.FILES['image']
        if form.is_valid():
            form.save()
            messages.success(request,"Malumotlaringiz o`zgartirildi")
            return redirect('restaurant_menu_admin')
    else:
        form = RestaurantMenuForm(instance=restaurant_menu)
        context = {'form': form }

        return render(request, 'restaurant_menu/restaurant_menu_edit.html', context)


def restaurant_menu_delate(request, id):
    restaurant_menu = Restaurant_menu.objects.get(pk=id)
    restaurant_menu.delete()
    messages.success(request,"Malumotlaringiz o'chirildi ")
    return redirect('aboutus_feature_admin')


#
# ────────────────────────────────────────────── I ──────────
#   :::::: S P A : :  :   :    :     :        :          :
# ────────────────────────────────────────────────────────
#



def spa_admin(request):
    spa = Spa.objects.all().order_by('id')

    context = {
        'spa': spa,
    }

    return render(request, 'spa/spa_admin.html', context)


def spa_create(request):
    spa = Spa()
    InlineFormSet = inlineformset_factory(Spa, Image_spa, form=SpaForm, fields=('image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = SpaForm(request.POST, request.FILES, instance=spa, prefix='spa')
        formset = InlineFormSet(request.POST, request.FILES, instance=spa, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request,"Malumotlaringiz qoshildi ")
            return redirect('spa_admin')

    else:
        form = SpaForm(instance=spa, prefix='spa')
        formset = InlineFormSet(instance=spa, prefix='images')
        
    context = {
        'form': form,
        'formset':formset,
    }
    return render(request, 'spa/spa_create.html', context)


def spa_edit(request, id):
    spa = Spa.objects.get(pk=id)
    InlineFormSet = inlineformset_factory(Spa, Image_spa, form=SpaForm, fields=('image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = SpaForm(request.POST, request.FILES, instance=spa, prefix='spa')
        formset = InlineFormSet(request.POST, request.FILES, instance=spa, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request,"Malumotlaringiz o`zgartirildi")
            return redirect('spa_admin')

    else:
        form = SpaForm(instance=spa, prefix='spa')
        formset = InlineFormSet(instance=spa, prefix='images')
        
    context = {
        'form': form,
        'formset':formset,
    }
    return render(request, 'spa/spa_edit.html', context)


def spa_delate(request, id):
    spa = Spa.objects.get(pk=id)
    spa.delete()
    messages.success(request,"Malumotlaringiz o'chirildi ")
    return redirect('spa_admin')



#
# ──────────────────────────────────────────────────────  ──────────
#   :::::: F I T N E S S : :  :   :    :     :        :          :
# ────────────────────────────────────────────────────────────────
#


def fitness_admin(request):
    fitness = Fitness.objects.all().order_by('id')

    context = {
        'fitness': fitness,
    }

    return render(request, 'fitness/fitness_admin.html', context)


def fitness_create(request):
    fitness = Fitness()
    InlineFormSet = inlineformset_factory(Fitness, Image_fitness, form=FitnessForm, fields=('image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = FitnessForm(request.POST, request.FILES, instance=fitness, prefix='fitness')
        formset = InlineFormSet(request.POST, request.FILES, instance=fitness, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request,"Malumotlaringiz qoshildi ")
            return redirect('fitness_admin')

    else:
        form = FitnessForm(instance=fitness, prefix='fitness')
        formset = InlineFormSet(instance=fitness, prefix='images')
        
    context = {
        'form': form,
        'formset':formset,
    }
    return render(request, 'fitness/fitness_create.html', context)


def fitness_edit(request, id):
    fitness = Fitness.objects.get(pk=id)
    InlineFormSet = inlineformset_factory(Fitness, Image_fitness, form=FitnessForm, fields=('image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = FitnessForm(request.POST, request.FILES, instance=fitness, prefix='fitness')
        formset = InlineFormSet(request.POST, request.FILES, instance=fitness, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request,"Malumotlaringiz o`zgartirildi")
            return redirect('fitness_admin')

    else:
        form = FitnessForm(instance=fitness, prefix='fitness')
        formset = InlineFormSet(instance=fitness, prefix='images')
        
    context = {
        'form': form,
        'formset':formset,
    }
    return render(request, 'fitness/fitness_edit.html', context)


def fitness_delate(request, id):
    fitness = Fitness.objects.get(pk=id)
    fitness.delete()
    messages.success(request,"Malumotlaringiz o'chirildi ")
    return redirect('fitness_admin')



#
# ──────────────────────────────────────────────────────────────────  ──────────
#   :::::: S P E C I A L   O F F E R : :  :   :    :     :        :          :
# ────────────────────────────────────────────────────────────────────────────
#


def special_offer_admin(request):
    special_offer = Special_offer.objects.all().order_by('id')

    context = {
        'special_offer': special_offer,
    }

    return render(request, 'special_offer/special_offer_admin.html', context)


def special_offer_create(request):
    special_offer = Special_offer()
    InlineFormSet = inlineformset_factory(Special_offer, Image_offer, form=SpecialOfferForm, fields=('image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = SpecialOfferForm(request.POST, request.FILES, instance=special_offer, prefix='special_offer')
        formset = InlineFormSet(request.POST, request.FILES, instance=special_offer, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request,"Malumotlaringiz qoshildi ")
            return redirect('special_offer_admin')

    else:
        form = SpecialOfferForm(instance=special_offer, prefix='special_offer')
        formset = InlineFormSet(instance=special_offer, prefix='images')
        
    context = {
        'form': form,
        'formset':formset,
    }
    return render(request, 'special_offer/special_offer_create.html', context)


def special_offer_edit(request, id):
    special_offer = Special_offer.objects.get(pk=id)
    InlineFormSet = inlineformset_factory(Special_offer, Image_offer, form=SpecialOfferForm, fields=('image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = SpecialOfferForm(request.POST, request.FILES, instance=special_offer, prefix='special_offer')
        formset = InlineFormSet(request.POST, request.FILES, instance=special_offer, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request,"Malumotlaringiz o`zgartirildi")
            return redirect('special_offer_admin')

    else:
        form = SpecialOfferForm(instance=special_offer, prefix='special_offer')
        formset = InlineFormSet(instance=special_offer, prefix='images')
        
    context = {
        'form': form,
        'formset':formset,
    }
    return render(request, 'special_offer/special_offer_edit.html', context)


def special_offer_delate(request, id):
    special_offer = Special_offer.objects.get(pk=id)
    special_offer.delete()
    messages.success(request,"Malumotlaringiz o'chirildi ")
    return redirect('special_offer_admin')



#
# ──────────────────────────────────────────────────────────────  ──────────
#   :::::: O F F E R   O R D E R : :  :   :    :     :        :          :
# ────────────────────────────────────────────────────────────────────────
#



def offer_order_admin(request):
    offer_order = Offer_order.objects.all().order_by('id')
    
    context = {
        'offer_order': offer_order,

    }

    return render(request, 'offer_order/offer_order_admin.html', context)




def offer_order_edit(request, id):
    offer_order = Offer_order.objects.get(pk=id)
    if request.method == 'POST':
        form = SpecialOfferAdminForm(request.POST, instance=offer_order)
        if form.is_valid():
            form.save()
            messages.success(request,"Malumotlaringiz o`zgartirildi")
            return redirect('offer_order_admin')
    else:
        form = SpecialOfferAdminForm(instance=offer_order)
        context = {'form': form }

        return render(request, 'offer_order/offer_order_edit.html', context)



#
# ────────────────────────────────────────────────────────────────────────  ──────────
#   :::::: C A T E G O R Y   G A L L E R Y : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────────────────────────────
#


def category_gallery_admin(request):
    category_gallery = Category_gallery.objects.all().order_by('id')

    context = {
        'category_gallery': category_gallery,

    }

    return render(request, 'category_gallery/category_gallery_admin.html', context)


def category_gallery_create(request):
    if request.method == 'POST':
        form = CategoryGalleryForm(request.POST)
        if form.is_valid():
            category_gallery = Category_gallery()
            category_gallery.title = form.cleaned_data.get('title')
            category_gallery.cat_filter = form.cleaned_data.get('cat_filter')
            category_gallery.save()
            messages.success(request,"Malumotlaringiz qoshildi ")
            return redirect('category_gallery_admin')
    form = CategoryGalleryForm()
    context = {
        'form': form,
    }
    return render(request, 'category_gallery/category_gallery_create.html', context)


def category_gallery_edit(request, id):
    category_gallery = Category_gallery.objects.get(pk=id)
    if request.method == 'POST':
        form = CategoryGalleryForm(request.POST,  instance=category_gallery)
        if form.is_valid():
            form.save()
            messages.success(request,"Malumotlaringiz o`zgartirildi")
            return redirect('category_gallery_admin')
    else:
        form = CategoryGalleryForm(instance=category_gallery)
        context = {'form': form }

        return render(request, 'category_gallery/category_gallery_edit.html', context)


def category_gallery_delate(request, id):
    category_gallery = Category_gallery.objects.get(pk=id)
    category_gallery.delete()
    messages.success(request,"Malumotlaringiz o'chirildi ")
    return redirect('category_gallery_admin')





#
# ────────────────────────────────────────────────────── I ──────────
#   :::::: G A L L E R Y : :  :   :    :     :        :          :
# ────────────────────────────────────────────────────────────────
#



def gallery_admin(request):
    gallery = Gallery.objects.all().order_by('id')

    context = {
        'gallery': gallery,

    }

    return render(request, 'gallery/gallery_admin.html', context)


def gallery_create(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            gallery = Gallery()
            gallery.title = form.cleaned_data.get('title')
            gallery.cat_filter = form.cleaned_data.get('cat_filter')
            gallery.category = form.cleaned_data.get('category')
            if request.FILES:
                gallery.image = request.FILES['image']
            gallery.save()
            messages.success(request,"Malumotlaringiz qoshildi ")
            return redirect('gallery_admin')
    form = GalleryForm()
    context = {
        'form': form,
    }
    return render(request, 'gallery/gallery_create.html', context)


def gallery_edit(request, id):
    gallery = Gallery.objects.get(pk=id)
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES, instance=gallery)
        if request.FILES:
            gallery.image = request.FILES['image']
        if form.is_valid():
            form.save()
            messages.success(request,"Malumotlaringiz o`zgartirildi")
            return redirect('gallery_admin')
    else:
        form = GalleryForm(instance=gallery)
        context = {'form': form }

        return render(request, 'gallery/gallery_edit.html', context)


def gallery_delate(request, id):
    gallery = Gallery.objects.get(pk=id)
    gallery.delete()
    messages.success(request,"Malumotlaringiz o'chirildi ")
    return redirect('gallery_admin')




#
# ────────────────────────────────────────────────────────────────────  ──────────
#   :::::: C A T E G O R Y   S T A F F : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────────────────────────
#


def category_staff_admin(request):
    category_staff = Category_staff.objects.all().order_by('id')

    context = {
        'category_staff': category_staff,

    }

    return render(request, 'category_staff/category_staff_admin.html', context)


def category_staff_create(request):
    if request.method == 'POST':
        form = CategoryStaffForm(request.POST)
        if form.is_valid():
            category_staff = Category_staff()
            category_staff.title = form.cleaned_data.get('title')
            category_staff.cat_filter = form.cleaned_data.get('cat_filter')
            category_staff.save()
            messages.success(request,"Malumotlaringiz qoshildi ")
            return redirect('category_staff_admin')
    form = CategoryStaffForm()
    context = {
        'form': form,
    }
    return render(request, 'category_staff/category_staff_create.html', context)


def category_staff_edit(request, id):
    category_staff = Category_staff.objects.get(pk=id)
    if request.method == 'POST':
        form = CategoryStaffForm(request.POST,  instance=category_staff)
        if form.is_valid():
            form.save()
            messages.success(request,"Malumotlaringiz o`zgartirildi")
            return redirect('category_staff_admin')
    else:
        form = CategoryStaffForm(instance=category_staff)
        context = {'form': form }

        return render(request, 'category_staff/category_staff_create.html', context)


def category_staff_delate(request, id):
    category_staff = Category_staff.objects.get(pk=id)
    category_staff.delete()
    messages.success(request,"Malumotlaringiz o'chirildi ")
    return redirect('category_staff_admin')




#
# ──────────────────────────────────────────────────────────  ──────────
#   :::::: O U R   S T A F F : :  :   :    :     :        :          :
# ────────────────────────────────────────────────────────────────────
#


def our_staff_admin(request):
    our_staff = Our_Staff.objects.all().order_by('id')

    context = {
        'our_staff': our_staff,

    }

    return render(request, 'our_staff/our_staff_admin.html', context)


def our_staff_create(request):
    if request.method == 'POST':
        form = OurStaffForm(request.POST, request.FILES)
        if form.is_valid():
            our_staff = Our_Staff()
            our_staff.name = form.cleaned_data.get('name')
            our_staff.surename = form.cleaned_data.get('surename')
            our_staff.phone = form.cleaned_data.get('phone')
            our_staff.description = form.cleaned_data.get('description')
            our_staff.profession = form.cleaned_data.get('profession')
            our_staff.category = form.cleaned_data.get('category')
            our_staff.status = form.cleaned_data.get('status')
            our_staff.telegram = form.cleaned_data.get('telegram')
            our_staff.instagram = form.cleaned_data.get('instagram')
            our_staff.facebook = form.cleaned_data.get('facebook')
            if request.FILES:
                our_staff.image = request.FILES['image']
            our_staff.save()
            messages.success(request,"Malumotlaringiz qoshildi ")
            return redirect('our_staff_admin')
    form = OurStaffForm()
    context = {
        'form': form,
    }
    return render(request, 'our_staff/our_staff_create.html', context)


def our_staff_edit(request, id):
    our_staff = Our_Staff.objects.get(pk=id)
    if request.method == 'POST':
        form = OurStaffForm(request.POST, request.FILES, instance=our_staff)
        if form.is_valid():
            if request.FILES:
                our_staff.image = request.FILES['image']
            form.save()
            messages.success(request,"Malumotlaringiz o`zgartirildi")
            return redirect('our_staff_admin')
    else:
        form = OurStaffForm(instance=our_staff)
        context = {'form': form }

        return render(request, 'our_staff/our_staff_edit.html', context)


def our_staff_delate(request, id):
    our_staff = Our_Staff.objects.get(pk=id)
    our_staff.delete()
    messages.success(request,"Malumotlaringiz o'chirildi ")
    return redirect('our_staff_admin')



#
# ──────────────────────────────────────────────────── I ──────────
#   :::::: E V E N T S : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────────
#


def events_admin(request):
    events = Events.objects.all().order_by('id')

    context = {
        'events': events,
    }

    return render(request, 'events/events_admin.html', context)


def event_create(request):
    events = Events()
    InlineFormSet = inlineformset_factory(Events, Image_events, form=EventsForm, fields=('image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = EventsForm(request.POST, request.FILES, instance=events, prefix='events')
        formset = InlineFormSet(request.POST, request.FILES, instance=events, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request,"Malumotlaringiz qoshildi ")
            return redirect('events_admin')

    else:
        form = EventsForm(instance=events, prefix='events')
        formset = InlineFormSet(instance=events, prefix='images')
        
    context = {
        'form': form,
        'formset':formset,
    }
    return render(request, 'events/event_create.html', context)


def event_edit(request, id):
    events = Events.objects.get(pk=id)
    InlineFormSet = inlineformset_factory(Events, Image_events, form=EventsForm, fields=('image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = EventsForm(request.POST, request.FILES, instance=events, prefix='events')
        formset = InlineFormSet(request.POST, request.FILES, instance=events, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request,"Malumotlaringiz o`zgartirildi")
            return redirect('events_admin')

    else:
        form = EventsForm(instance=events, prefix='events')
        formset = InlineFormSet(instance=events, prefix='images')
        
    context = {
        'form': form,
        'formset':formset,
    }
    return render(request, 'events/event_edit.html', context)


def event_delate(request, id):
    events = Events.objects.get(pk=id)
    events.delete()
    messages.success(request,"Malumotlaringiz o'chirildi ")
    return redirect('events_admin')




#
# ────────────────────────────────────────────────── I ──────────
#   :::::: P L A C E : :  :   :    :     :        :          :
# ────────────────────────────────────────────────────────────
#



def place_admin(request):
    places = Place.objects.all().order_by('id')

    context = {
        'places': places,
    }

    return render(request, 'places/place_admin.html', context)


def place_create(request):
    places = Place()
    InlineFormSet = inlineformset_factory(Place, Image_place, form=PlaceForm, fields=('image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES, instance=places, prefix='places')
        formset = InlineFormSet(request.POST, request.FILES, instance=places, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request,"Malumotlaringiz qoshildi ")
            return redirect('place_admin')

    else:
        form = PlaceForm(instance=places, prefix='places')
        formset = InlineFormSet(instance=places, prefix='images')
        
    context = {
        'form': form,
        'formset':formset,
    }
    return render(request, 'places/place_create.html', context)


def place_edit(request, id):
    places = Place.objects.get(pk=id)
    InlineFormSet = inlineformset_factory(Place, Image_place, form=PlaceForm, fields=('image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES, instance=places, prefix='places')
        formset = InlineFormSet(request.POST, request.FILES, instance=places, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request,"Malumotlaringiz o`zgartirildi")
            return redirect('place_admin')

    else:
        form = PlaceForm(instance=places, prefix='places')
        formset = InlineFormSet(instance=places, prefix='images')
        
    context = {
        'form': form,
        'formset':formset,
    }
    return render(request, 'places/place_edit.html', context)


def place_delate(request, id):
    places = Place.objects.get(pk=id)
    places.delete()
    messages.success(request,"Malumotlaringiz o'chirildi ")
    return redirect('place_admin')
