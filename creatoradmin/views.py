
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.admin.views.decorators import user_passes_test


from room.models import Order, Room, RoomServices, Room_Image
from home.models import Slider, AboutUs, Image_aboutus, AboutUs_features, License, LicImages
from creatoradmin.forms import *
from service.models import Business, Image_business, Image_events, Image_fitness, Image_offer, Image_place, Image_restaurant, Image_spa, Service, Image_service


# -------------------------- Admin Required Function ------------------------- #


def admin_required(view_func=None, login_url='login_form'):

    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.user_type == 3,
        login_url=login_url,
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator

# ---------------------------------------------------------------------------- #


# ---------------------- Registration Required Function ---------------------- #


def registration_required(view_func=None, login_url='login_form'):

    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and (
            u.user_type == 2 or u.user_type == 3),
        login_url=login_url,
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator


# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
#                                ADMIN DASHBOARD                               #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


def admin_panel(requset):
    order_room = Order.objects.all().filter(status="New")
    offer_order = Offer_order.objects.all().filter(status="New")
    order_events = Offer_events_ticket.objects.all().filter(status="New")
    contact_message = ContactMessage.objects.all().filter(status="New")

    context = {
        'order_room': order_room,
        'offer_order': offer_order,
        'order_events': order_events,
        'contact_message': contact_message

    }
    return render(requset, 'admindemo.html', context)


# ---------------------------------------------------------------------------- #
#                                   USER TYPE                                  #
# ---------------------------------------------------------------------------- #


def users_admin(request):
    users = CustomUser.objects.all()

    context = {
        'users': users
    }
    return render(request, 'users/users_admin.html', context)


def user_edit(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserTypeChangeForm(request.POST, request.FILES, instance=user)
        if request.FILES:
            user.avatar = request.FILES['avatar']
        if form.is_valid():
            form.save()
            return redirect('users_admin')
    else:
        form = UserTypeChangeForm(instance=user)
    context = {
        'user': user,
        'form': form,
    }
    return render(request, 'users/user_edit.html', context)


def user_detail(request, user_id):
    user = CustomUser.objects.filter(id=user_id)

    context = {
        'user': user
    }
    return render(request, 'users/user_detail.html', context)


def user_delete(request, user_id):
    user = CustomUser.objects.filter(id=user_id)
    user.delete()
    return redirect('users_admin')

# ---------------------------------------------------------------------------- #
#                                  Room Slider                                 #
# ---------------------------------------------------------------------------- #


@registration_required
def sliders(request):
    sliders = Slider.objects.all()

    context = {
        'sliders': sliders
    }
    return render(request, 'slider/sliders.html', context)


@admin_required
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


@admin_required
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
        context = {'form': form, }

        return render(request, 'slider/slider_edit.html', context)


@admin_required
def slider_delate(request, id):
    slider = Slider.objects.get(pk=id)
    slider.delete()
    return redirect('sliders')


# ---------------------------------------------------------------------------- #
#                                     Room                                     #
# ---------------------------------------------------------------------------- #


@registration_required
def room(request):
    rooms = Room.objects.all()

    context = {
        'rooms': rooms
    }
    return render(request, 'room/room.html', context)


@admin_required
def room_create(request):
    room_forms = Room()
    RoomInlineFormSet = inlineformset_factory(Room, Room_Image, form=RoomSliderForm, fields=(
        'room', 'image',), extra=5, can_delete=False, min_num=1, validate_min=True)
    RoomServiceFormSet = inlineformset_factory(Room, RoomServices, form=RoomServiceForm, fields=(
        'title', 'description', 'icon',), extra=2, can_delete=False, min_num=1, validate_min=True)
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES,
                        instance=room_forms, prefix='room')
        formset = RoomInlineFormSet(
            request.POST, request.FILES, instance=room_forms, prefix='images')
        formset2 = RoomServiceFormSet(
            request.POST, instance=room_forms, prefix='services')
        if all([form.is_valid(), formset.is_valid(), formset2.is_valid(), ],):
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
        'formset': formset,
        'formset2': formset2
    }
    return render(request, 'room/room_create.html', context)


@admin_required
def room_edit(request, id):
    room = Room.objects.get(pk=id)
    RoomInlineFormSet = inlineformset_factory(Room, Room_Image, form=RoomSliderForm, fields=(
        'room', 'image',), extra=5, can_delete=True, min_num=1, validate_min=True)
    RoomServiceFormSet = inlineformset_factory(Room, RoomServices, form=RoomServiceForm, fields=(
        'title', 'description', 'icon',), extra=2, can_delete=False, min_num=1, validate_min=True)
    if request.method == 'POST':

        form = RoomForm(request.POST, request.FILES,
                        instance=room, prefix='room')
        formset = RoomInlineFormSet(
            request.POST, request.FILES, instance=room, prefix='images')
        formset2 = RoomServiceFormSet(
            request.POST, instance=room, prefix='services')

        if all([form.is_valid(), formset.is_valid(), formset2.is_valid(), ],):
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
        'formset': formset,
        'formset2': formset2
    }

    return render(request, 'room/room_edit.html', context)


@admin_required
def room_delate(request, id):
    room = Room.objects.get(pk=id)
    room.delete()
    return redirect('rooms_admin')


# ---------------------------------------------------------------------------- #
#                                Categories Room                               #
# ---------------------------------------------------------------------------- #


def categories(request):
    categories = Category.objects.all()

    context = {
        'categories': categories
    }
    return render(request, 'category_room/categories.html', context)


@admin_required
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


@admin_required
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
        context = {'form': form, }

        return render(request, 'category_room/category_edit.html', context)


@admin_required
def category_delate(request, id):
    category = Category.objects.get(pk=id)
    category.delete()
    return redirect('categories')


# ---------------------------------------------------------------------------- #
#                                Categories Blog                               #
# ---------------------------------------------------------------------------- #


@admin_required
def categories_blog(request):
    categories_blog = Category_Blog.objects.all()

    context = {
        'categories_blog': categories_blog
    }
    return render(request, 'category_blog/categories_blog.html', context)


@admin_required
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


@admin_required
def category_blog_edit(request, id):
    category_blog = Category_Blog.objects.get(pk=id)
    if request.method == 'POST':
        form = CategoryBlogForm(request.POST, instance=category_blog)
        if form.is_valid():
            form.save()
            return redirect('categories_blog')
    else:
        form = CategoryBlogForm(instance=category_blog)
        context = {'form': form, }

        return render(request, 'category_blog/category_blog_edit.html', context)


@admin_required
def category_blog_delate(request, id):
    category_blog = Category_Blog.objects.get(pk=id)
    category_blog.delete()
    return redirect('categories_blog')


# ---------------------------------------------------------------------------- #
#                                     Blog                                     #
# ---------------------------------------------------------------------------- #


@registration_required
def blogs(request):
    blogs = Blog.objects.all().order_by('id')

    context = {
        'blogs': blogs,

    }

    return render(request, 'blog/blogs.html', context)


@admin_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = Blog()
            current_user = request.user
            blog.author_id = current_user.id
            blog.title = form.cleaned_data.get('title')
            blog.description = form.cleaned_data.get('description')
            blog.text = form.cleaned_data.get('text')
            blog.category = form.cleaned_data.get('category')
            if request.FILES:
                blog.image = request.FILES['image']
            blog.status = form.cleaned_data.get('status')
            blog.save()
            return redirect('blogs_admin')
    form = BlogForm()
    context = {
        'form': form,
    }
    return render(request, 'blog/blog_create.html', context)


@admin_required
def blog_edit(request, id):
    blog = Blog.objects.get(pk=id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if request.FILES:
            blog.image = request.FILES['image']
        if form.is_valid():
            form.save()
            return redirect('blogs_admin')
    else:
        form = BlogForm(instance=blog)
        context = {'form': form}

        return render(request, 'blog/blog_edit.html', context)


@admin_required
def blog_delate(request, id):
    blog = Blog.objects.get(pk=id)
    blog.delete()
    return redirect('blogs_admin')


# ---------------------------------------------------------------------------- #
#                                   Services                                   #
# ---------------------------------------------------------------------------- #


@admin_required
def services(request):
    services = Service.objects.all().order_by('id')

    context = {
        'services': services,

    }

    return render(request, 'service/services.html', context)


@admin_required
def service_create(request):
    services = Service()
    RoomInlineFormSet = inlineformset_factory(Service, Image_service, form=ServiceForm, fields=(
        'image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES,
                           instance=services, prefix='service')
        formset = RoomInlineFormSet(
            request.POST, request.FILES, instance=services, prefix='images')
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
        'formset': formset,
    }
    return render(request, 'service/service_create.html', context)


@admin_required
def service_edit(request, id):
    service = Service.objects.get(pk=id)
    RoomInlineFormSet = inlineformset_factory(Service, Image_service, form=ServiceForm, fields=(
        'image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES,
                           instance=service, prefix='service')
        formset = RoomInlineFormSet(
            request.POST, request.FILES, instance=service, prefix='images')
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
        'formset': formset,
    }
    return render(request, 'service/service_edit.html', context)


@admin_required
def service_delate(request, id):
    service = Service.objects.get(pk=id)
    service.delete()
    return redirect('services_admin')


# ---------------------------------------------------------------------------- #
#                                   About Us                                   #
# ---------------------------------------------------------------------------- #


@admin_required
def aboutus_admin(request):
    aboutus = AboutUs.objects.all().order_by('id')

    context = {
        'aboutus': aboutus,

    }

    return render(request, 'aboutus/aboutus_admin.html', context)


@admin_required
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


@admin_required
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
        context = {'form': form}

        return render(request, 'aboutus/aboutus_edit.html', context)


@admin_required
def aboutus_delate(request, id):
    aboutus = AboutUs.objects.get(pk=id)
    aboutus.delete()
    return redirect('aboutus_admin')


# ---------------------------------------------------------------------------- #
#                                About Us Image                                #
# ---------------------------------------------------------------------------- #


@admin_required
def aboutus_image_admin(request):
    aboutus_images = Image_aboutus.objects.all().order_by('id')

    context = {
        'aboutus_images': aboutus_images,

    }

    return render(request, 'aboutus_image/aboutus_image_admin.html', context)


@admin_required
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


@admin_required
def aboutus_image_edit(request, id):
    aboutus_image = Image_aboutus.objects.get(pk=id)
    if request.method == 'POST':
        form = AboutUsImageForm(
            request.POST, request.FILES, instance=aboutus_image)
        if request.FILES:
            aboutus_image.image = request.FILES['image']
        if form.is_valid():
            form.save()
            return redirect('aboutus_image_admin')
    else:
        form = AboutUsImageForm(instance=aboutus_image)
        context = {'form': form}

        return render(request, 'aboutus_image/aboutus_image_edit.html', context)


@admin_required
def aboutus_image_delate(request, id):
    aboutus_image = Image_aboutus.objects.get(pk=id)
    aboutus_image.delete()
    return redirect('aboutus_image_admin')


# ---------------------------------------------------------------------------- #
#                                Aboutus Feature                               #
# ---------------------------------------------------------------------------- #


@admin_required
def aboutus_feature_admin(request):
    aboutus_features = AboutUs_features.objects.all().order_by('id')

    context = {
        'aboutus_features': aboutus_features,

    }

    return render(request, 'aboutus_feature/aboutus_feature_admin.html', context)


@admin_required
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


@admin_required
def aboutus_feature_edit(request, id):
    aboutus_feature = AboutUs_features.objects.get(pk=id)
    if request.method == 'POST':
        form = AboutUsFeatureForm(
            request.POST, request.FILES, instance=aboutus_feature)
        if request.FILES:
            aboutus_feature.image = request.FILES['image']
        if form.is_valid():
            form.save()
            return redirect('aboutus_feature_admin')
    else:
        form = AboutUsFeatureForm(instance=aboutus_feature)
        context = {'form': form}

        return render(request, 'aboutus_feature/aboutus_feature_edit.html', context)


@admin_required
def aboutus_feature_delate(request, id):
    aboutus_feature = AboutUs_features.objects.get(pk=id)
    aboutus_feature.delete()
    return redirect('aboutus_feature_admin')


# ---------------------------------------------------------------------------- #
#                                   Business                                   #
# ---------------------------------------------------------------------------- #


@admin_required
def business_admin(request):
    business = Business.objects.all().order_by('id')

    context = {
        'business': business,
    }

    return render(request, 'business/business_admin.html', context)


@admin_required
def business_create(request):
    business = Business()
    InlineFormSet = inlineformset_factory(Business, Image_business, form=BusinessForm, fields=(
        'image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES,
                            instance=business, prefix='business')
        formset = InlineFormSet(
            request.POST, request.FILES, instance=business, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request, "Malumotlaringiz qoshildi ")
            return redirect('business_admin')

    else:
        form = BusinessForm(instance=business, prefix='business')
        formset = InlineFormSet(instance=business, prefix='images')

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'business/business_create.html', context)


@admin_required
def business_edit(request, id):
    business = Business.objects.get(pk=id)
    InlineFormSet = inlineformset_factory(Business, Image_business, form=BusinessForm, fields=(
        'image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES,
                            instance=business, prefix='business')
        formset = InlineFormSet(
            request.POST, request.FILES, instance=business, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request, "Malumotlaringiz o`zgartirildi")
            return redirect('business_admin')

    else:
        form = BusinessForm(instance=business, prefix='business')
        formset = InlineFormSet(instance=business, prefix='images')

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'business/business_edit.html', context)


@admin_required
def business_delate(request, id):
    business = Business.objects.get(pk=id)
    business.delete()
    messages.success(request, "Malumotlaringiz o'chirildi ")
    return redirect('business_admin')


# ---------------------------------------------------------------------------- #
#                                  Restaurant                                  #
# ---------------------------------------------------------------------------- #


@admin_required
def restaurant_admin(request):
    restaurant = Restaurant.objects.all().order_by('id')

    context = {
        'restaurant': restaurant,
    }

    return render(request, 'restaurant/restaurant_admin.html', context)


@admin_required
def restaurant_create(request):
    restaurant = Restaurant()
    InlineFormSet = inlineformset_factory(Restaurant, Image_restaurant, form=RestaurantForm, fields=(
        'image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES,
                              instance=restaurant, prefix='restaurant')
        formset = InlineFormSet(
            request.POST, request.FILES, instance=restaurant, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request, "Malumotlaringiz qoshildi ")
            return redirect('restaurant_admin')

    else:
        form = RestaurantForm(instance=restaurant, prefix='restaurant')
        formset = InlineFormSet(instance=restaurant, prefix='images')

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'restaurant/restaurant_create.html', context)


@admin_required
def restaurant_edit(request, id):
    restaurant = Restaurant.objects.get(pk=id)
    InlineFormSet = inlineformset_factory(Restaurant, Image_restaurant, form=RestaurantForm, fields=(
        'image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES,
                              instance=restaurant, prefix='restaurant')
        formset = InlineFormSet(
            request.POST, request.FILES, instance=restaurant, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request, "Malumotlaringiz o`zgartirildi")
            return redirect('restaurant_admin')

    else:
        form = RestaurantForm(instance=restaurant, prefix='restaurant')
        formset = InlineFormSet(instance=restaurant, prefix='images')

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'restaurant/restaurant_edit.html', context)


@admin_required
def restaurant_delate(request, id):
    restaurant = Restaurant.objects.get(pk=id)
    restaurant.delete()
    messages.success(request, "Malumotlaringiz o'chirildi ")
    return redirect('restaurant_admin')


# ---------------------------------------------------------------------------- #
#                                Restaurant Menu                               #
# ---------------------------------------------------------------------------- #


@admin_required
def restaurant_menu_admin(request):
    restaurant_menu = Restaurant_menu.objects.all().order_by('id')

    context = {
        'restaurant_menu': restaurant_menu,

    }

    return render(request, 'restaurant_menu/restaurant_menu_admin.html', context)


@admin_required
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
            messages.success(request, "Malumotlaringiz qoshildi ")
            return redirect('restaurant_menu_admin')
    form = RestaurantMenuForm()
    context = {
        'form': form,
    }
    return render(request, 'restaurant_menu/restaurant_menu_create.html', context)


@admin_required
def restaurant_menu_edit(request, id):
    restaurant_menu = Restaurant_menu.objects.get(pk=id)
    if request.method == 'POST':
        form = RestaurantMenuForm(
            request.POST, request.FILES, instance=restaurant_menu)
        if request.FILES:
            restaurant_menu.image = request.FILES['image']
        if form.is_valid():
            form.save()
            messages.success(request, "Malumotlaringiz o`zgartirildi")
            return redirect('restaurant_menu_admin')
    else:
        form = RestaurantMenuForm(instance=restaurant_menu)
        context = {'form': form}

        return render(request, 'restaurant_menu/restaurant_menu_edit.html', context)


@admin_required
def restaurant_menu_delate(request, id):
    restaurant_menu = Restaurant_menu.objects.get(pk=id)
    restaurant_menu.delete()
    messages.success(request, "Malumotlaringiz o'chirildi ")
    return redirect('aboutus_feature_admin')


# ---------------------------------------------------------------------------- #
#                                      SPA                                     #
# ---------------------------------------------------------------------------- #


@admin_required
def spa_admin(request):
    spa = Spa.objects.all().order_by('id')

    context = {
        'spa': spa,
    }

    return render(request, 'spa/spa_admin.html', context)


@admin_required
def spa_create(request):
    spa = Spa()
    InlineFormSet = inlineformset_factory(Spa, Image_spa, form=SpaForm, fields=(
        'image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = SpaForm(request.POST, request.FILES, instance=spa, prefix='spa')
        formset = InlineFormSet(
            request.POST, request.FILES, instance=spa, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request, "Malumotlaringiz qoshildi ")
            return redirect('spa_admin')

    else:
        form = SpaForm(instance=spa, prefix='spa')
        formset = InlineFormSet(instance=spa, prefix='images')

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'spa/spa_create.html', context)


@admin_required
def spa_edit(request, id):
    spa = Spa.objects.get(pk=id)
    InlineFormSet = inlineformset_factory(Spa, Image_spa, form=SpaForm, fields=(
        'image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = SpaForm(request.POST, request.FILES, instance=spa, prefix='spa')
        formset = InlineFormSet(
            request.POST, request.FILES, instance=spa, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request, "Malumotlaringiz o`zgartirildi")
            return redirect('spa_admin')

    else:
        form = SpaForm(instance=spa, prefix='spa')
        formset = InlineFormSet(instance=spa, prefix='images')

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'spa/spa_edit.html', context)


@admin_required
def spa_delate(request, id):
    spa = Spa.objects.get(pk=id)
    spa.delete()
    messages.success(request, "Malumotlaringiz o'chirildi ")
    return redirect('spa_admin')


# ---------------------------------------------------------------------------- #
#                                    Fitness                                   #
# ---------------------------------------------------------------------------- #


@admin_required
def fitness_admin(request):
    fitness = Fitness.objects.all().order_by('id')

    context = {
        'fitness': fitness,
    }

    return render(request, 'fitness/fitness_admin.html', context)


@admin_required
def fitness_create(request):
    fitness = Fitness()
    InlineFormSet = inlineformset_factory(Fitness, Image_fitness, form=FitnessForm, fields=(
        'image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = FitnessForm(request.POST, request.FILES,
                           instance=fitness, prefix='fitness')
        formset = InlineFormSet(
            request.POST, request.FILES, instance=fitness, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request, "Malumotlaringiz qoshildi ")
            return redirect('fitness_admin')

    else:
        form = FitnessForm(instance=fitness, prefix='fitness')
        formset = InlineFormSet(instance=fitness, prefix='images')

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'fitness/fitness_create.html', context)


@admin_required
def fitness_edit(request, id):
    fitness = Fitness.objects.get(pk=id)
    InlineFormSet = inlineformset_factory(Fitness, Image_fitness, form=FitnessForm, fields=(
        'image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = FitnessForm(request.POST, request.FILES,
                           instance=fitness, prefix='fitness')
        formset = InlineFormSet(
            request.POST, request.FILES, instance=fitness, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request, "Malumotlaringiz o`zgartirildi")
            return redirect('fitness_admin')

    else:
        form = FitnessForm(instance=fitness, prefix='fitness')
        formset = InlineFormSet(instance=fitness, prefix='images')

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'fitness/fitness_edit.html', context)


@admin_required
def fitness_delate(request, id):
    fitness = Fitness.objects.get(pk=id)
    fitness.delete()
    messages.success(request, "Malumotlaringiz o'chirildi ")
    return redirect('fitness_admin')


# ---------------------------------------------------------------------------- #
#                                 Special Offer                                #
# ---------------------------------------------------------------------------- #


@admin_required
def special_offer_admin(request):
    special_offer = Special_offer.objects.all().order_by('id')

    context = {
        'special_offer': special_offer,
    }

    return render(request, 'special_offer/special_offer_admin.html', context)


@admin_required
def special_offer_create(request):
    special_offer = Special_offer()
    InlineFormSet = inlineformset_factory(Special_offer, Image_offer, form=SpecialOfferForm, fields=(
        'image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = SpecialOfferForm(
            request.POST, request.FILES, instance=special_offer, prefix='special_offer')
        formset = InlineFormSet(
            request.POST, request.FILES, instance=special_offer, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request, "Malumotlaringiz qoshildi ")
            return redirect('special_offer_admin')

    else:
        form = SpecialOfferForm(instance=special_offer, prefix='special_offer')
        formset = InlineFormSet(instance=special_offer, prefix='images')

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'special_offer/special_offer_create.html', context)


@admin_required
def special_offer_edit(request, id):
    special_offer = Special_offer.objects.get(pk=id)
    InlineFormSet = inlineformset_factory(Special_offer, Image_offer, form=SpecialOfferForm, fields=(
        'image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = SpecialOfferForm(
            request.POST, request.FILES, instance=special_offer, prefix='special_offer')
        formset = InlineFormSet(
            request.POST, request.FILES, instance=special_offer, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request, "Malumotlaringiz o`zgartirildi")
            return redirect('special_offer_admin')

    else:
        form = SpecialOfferForm(instance=special_offer, prefix='special_offer')
        formset = InlineFormSet(instance=special_offer, prefix='images')

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'special_offer/special_offer_edit.html', context)


@admin_required
def special_offer_delate(request, id):
    special_offer = Special_offer.objects.get(pk=id)
    special_offer.delete()
    messages.success(request, "Malumotlaringiz o'chirildi ")
    return redirect('special_offer_admin')


# ---------------------------------------------------------------------------- #
#                                  Offer Order                                 #
# ---------------------------------------------------------------------------- #


@admin_required
def offer_order_admin(request):
    offer_order = Offer_order.objects.all().order_by('id')

    context = {
        'offer_order': offer_order,

    }

    return render(request, 'offer_order/offer_order_admin.html', context)


@admin_required
def offer_order_edit(request, id):
    offer_order = Offer_order.objects.get(pk=id)
    if request.method == 'POST':
        form = SpecialOfferAdminForm(request.POST, instance=offer_order)
        if form.is_valid():
            form.save()
            messages.success(request, "Malumotlaringiz o`zgartirildi")
            return redirect('offer_order_admin')
    else:
        form = SpecialOfferAdminForm(instance=offer_order)
        context = {'form': form}

        return render(request, 'offer_order/offer_order_edit.html', context)


# ---------------------------------------------------------------------------- #
#                               Category Gallery                               #
# ---------------------------------------------------------------------------- #


@admin_required
def category_gallery_admin(request):
    category_gallery = Category_gallery.objects.all().order_by('id')

    context = {
        'category_gallery': category_gallery,

    }

    return render(request, 'category_gallery/category_gallery_admin.html', context)


@admin_required
def category_gallery_create(request):
    if request.method == 'POST':
        form = CategoryGalleryForm(request.POST)
        if form.is_valid():
            category_gallery = Category_gallery()
            category_gallery.title = form.cleaned_data.get('title')
            category_gallery.cat_filter = form.cleaned_data.get('cat_filter')
            category_gallery.save()
            messages.success(request, "Malumotlaringiz qoshildi ")
            return redirect('category_gallery_admin')
    form = CategoryGalleryForm()
    context = {
        'form': form,
    }
    return render(request, 'category_gallery/category_gallery_create.html', context)


@admin_required
def category_gallery_edit(request, id):
    category_gallery = Category_gallery.objects.get(pk=id)
    if request.method == 'POST':
        form = CategoryGalleryForm(request.POST,  instance=category_gallery)
        if form.is_valid():
            form.save()
            messages.success(request, "Malumotlaringiz o`zgartirildi")
            return redirect('category_gallery_admin')
    else:
        form = CategoryGalleryForm(instance=category_gallery)
        context = {'form': form}

        return render(request, 'category_gallery/category_gallery_edit.html', context)


@admin_required
def category_gallery_delate(request, id):
    category_gallery = Category_gallery.objects.get(pk=id)
    category_gallery.delete()
    messages.success(request, "Malumotlaringiz o'chirildi ")
    return redirect('category_gallery_admin')


# ---------------------------------------------------------------------------- #
#                                    Gallery                                   #
# ---------------------------------------------------------------------------- #


@admin_required
def gallery_admin(request):
    gallery = Gallery.objects.all().order_by('id')

    context = {
        'gallery': gallery,

    }

    return render(request, 'gallery/gallery_admin.html', context)


@admin_required
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
            messages.success(request, "Malumotlaringiz qoshildi ")
            return redirect('gallery_admin')
    form = GalleryForm()
    context = {
        'form': form,
    }
    return render(request, 'gallery/gallery_create.html', context)


@admin_required
def gallery_edit(request, id):
    gallery = Gallery.objects.get(pk=id)
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES, instance=gallery)
        if request.FILES:
            gallery.image = request.FILES['image']
        if form.is_valid():
            form.save()
            messages.success(request, "Malumotlaringiz o`zgartirildi")
            return redirect('gallery_admin')
    else:
        form = GalleryForm(instance=gallery)
        context = {'form': form}

        return render(request, 'gallery/gallery_edit.html', context)


@admin_required
def gallery_delate(request, id):
    gallery = Gallery.objects.get(pk=id)
    gallery.delete()
    messages.success(request, "Malumotlaringiz o'chirildi ")
    return redirect('gallery_admin')


# ---------------------------------------------------------------------------- #
#                                Category Staff                                #
# ---------------------------------------------------------------------------- #


@admin_required
def category_staff_admin(request):
    category_staff = Category_staff.objects.all().order_by('id')

    context = {
        'category_staff': category_staff,

    }

    return render(request, 'category_staff/category_staff_admin.html', context)


@admin_required
def category_staff_create(request):
    if request.method == 'POST':
        form = CategoryStaffForm(request.POST)
        if form.is_valid():
            category_staff = Category_staff()
            category_staff.title = form.cleaned_data.get('title')
            category_staff.cat_filter = form.cleaned_data.get('cat_filter')
            category_staff.save()
            messages.success(request, "Malumotlaringiz qoshildi ")
            return redirect('category_staff_admin')
    form = CategoryStaffForm()
    context = {
        'form': form,
    }
    return render(request, 'category_staff/category_staff_create.html', context)


@admin_required
def category_staff_edit(request, id):
    category_staff = Category_staff.objects.get(pk=id)
    if request.method == 'POST':
        form = CategoryStaffForm(request.POST,  instance=category_staff)
        if form.is_valid():
            form.save()
            messages.success(request, "Malumotlaringiz o`zgartirildi")
            return redirect('category_staff_admin')
    else:
        form = CategoryStaffForm(instance=category_staff)
        context = {'form': form}

        return render(request, 'category_staff/category_staff_create.html', context)


@admin_required
def category_staff_delate(request, id):
    category_staff = Category_staff.objects.get(pk=id)
    category_staff.delete()
    messages.success(request, "Malumotlaringiz o'chirildi ")
    return redirect('category_staff_admin')


# ---------------------------------------------------------------------------- #
#                                   Our Staff                                  #
# ---------------------------------------------------------------------------- #


@admin_required
def our_staff_admin(request):
    our_staff = Our_Staff.objects.all().order_by('id')

    context = {
        'our_staff': our_staff,

    }

    return render(request, 'our_staff/our_staff_admin.html', context)


@admin_required
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
            messages.success(request, "Malumotlaringiz qoshildi ")
            return redirect('our_staff_admin')
    form = OurStaffForm()
    context = {
        'form': form,
    }
    return render(request, 'our_staff/our_staff_create.html', context)


@admin_required
def our_staff_edit(request, id):
    our_staff = Our_Staff.objects.get(pk=id)
    if request.method == 'POST':
        form = OurStaffForm(request.POST, request.FILES, instance=our_staff)
        if form.is_valid():
            if request.FILES:
                our_staff.image = request.FILES['image']
            form.save()
            messages.success(request, "Malumotlaringiz o`zgartirildi")
            return redirect('our_staff_admin')
    else:
        form = OurStaffForm(instance=our_staff)
        context = {'form': form}

        return render(request, 'our_staff/our_staff_edit.html', context)


@admin_required
def our_staff_delate(request, id):
    our_staff = Our_Staff.objects.get(pk=id)
    our_staff.delete()
    messages.success(request, "Malumotlaringiz o'chirildi ")
    return redirect('our_staff_admin')


# ---------------------------------------------------------------------------- #
#                                    Events                                    #
# ---------------------------------------------------------------------------- #


@admin_required
def events_admin(request):
    events = Events.objects.all().order_by('id')

    context = {
        'events': events,
    }

    return render(request, 'events/events_admin.html', context)


@admin_required
def event_create(request):
    events = Events()
    InlineFormSet = inlineformset_factory(Events, Image_events, form=EventsForm, fields=(
        'image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = EventsForm(request.POST, request.FILES,
                          instance=events, prefix='events')
        formset = InlineFormSet(
            request.POST, request.FILES, instance=events, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request, "Malumotlaringiz qoshildi ")
            return redirect('events_admin')

    else:
        form = EventsForm(instance=events, prefix='events')
        formset = InlineFormSet(instance=events, prefix='images')

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'events/event_create.html', context)


@admin_required
def event_edit(request, id):
    events = Events.objects.get(pk=id)
    InlineFormSet = inlineformset_factory(Events, Image_events, form=EventsForm, fields=(
        'image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = EventsForm(request.POST, request.FILES,
                          instance=events, prefix='events')
        formset = InlineFormSet(
            request.POST, request.FILES, instance=events, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request, "Malumotlaringiz o`zgartirildi")
            return redirect('events_admin')

    else:
        form = EventsForm(instance=events, prefix='events')
        formset = InlineFormSet(instance=events, prefix='images')

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'events/event_edit.html', context)


@admin_required
def event_delate(request, id):
    events = Events.objects.get(pk=id)
    events.delete()
    messages.success(request, "Malumotlaringiz o'chirildi ")
    return redirect('events_admin')


# ---------------------------------------------------------------------------- #
#                                     Place                                    #
# ---------------------------------------------------------------------------- #


@admin_required
def place_admin(request):
    places = Place.objects.all().order_by('id')

    context = {
        'places': places,
    }

    return render(request, 'places/place_admin.html', context)


@admin_required
def place_create(request):
    places = Place()
    InlineFormSet = inlineformset_factory(Place, Image_place, form=PlaceForm, fields=(
        'image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES,
                         instance=places, prefix='places')
        formset = InlineFormSet(
            request.POST, request.FILES, instance=places, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request, "Malumotlaringiz qoshildi ")
            return redirect('place_admin')

    else:
        form = PlaceForm(instance=places, prefix='places')
        formset = InlineFormSet(instance=places, prefix='images')

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'places/place_create.html', context)


@admin_required
def place_edit(request, id):
    places = Place.objects.get(pk=id)
    InlineFormSet = inlineformset_factory(Place, Image_place, form=PlaceForm, fields=(
        'image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES,
                         instance=places, prefix='places')
        formset = InlineFormSet(
            request.POST, request.FILES, instance=places, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request, "Malumotlaringiz o`zgartirildi")
            return redirect('place_admin')

    else:
        form = PlaceForm(instance=places, prefix='places')
        formset = InlineFormSet(instance=places, prefix='images')

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'places/place_edit.html', context)


@admin_required
def place_delate(request, id):
    places = Place.objects.get(pk=id)
    places.delete()
    messages.success(request, "Malumotlaringiz o'chirildi ")
    return redirect('place_admin')


# ---------------------------------------------------------------------------- #
#                                  Testimonial                                 #
# ---------------------------------------------------------------------------- #


@admin_required
def testimonial_admin(request):
    testimonials = Testimonial.objects.all().order_by('id')

    context = {
        'testimonials': testimonials,

    }

    return render(request, 'testimonials/testimonial_admin.html', context)


@admin_required
def testimonial_create(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            testimonial = Testimonial()
            testimonial.name = form.cleaned_data.get('name')
            testimonial.location = form.cleaned_data.get('location')
            testimonial.description = form.cleaned_data.get('description')
            testimonial.rating = form.cleaned_data.get('rating')
            testimonial.status = form.cleaned_data.get('status')
            if request.FILES:
                testimonial.photo = request.FILES['photo']
            testimonial.save()
            messages.success(request, "Malumotlaringiz qoshildi ")
            return redirect('testimonial_admin')
    form = TestimonialForm()
    context = {
        'form': form,
    }
    return render(request, 'testimonials/testimonial_create.html', context)


@admin_required
def testimonial_edit(request, id):
    testimonial = Testimonial.objects.get(pk=id)
    if request.method == 'POST':
        form = TestimonialForm(
            request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            if request.FILES:
                testimonial.photo = request.FILES['photo']
            form.save()
            messages.success(request, "Malumotlaringiz o`zgartirildi")
            return redirect('testimonial_admin')
    else:
        form = TestimonialForm(instance=testimonial)
        context = {'form': form}

        return render(request, 'testimonials/testimonial_edit.html', context)


@admin_required
def testimonial_delate(request, id):
    testimonial = Testimonial.objects.get(pk=id)
    testimonial.delete()
    messages.success(request, "Malumotlaringiz o'chirildi ")
    return redirect('testimonial_admin')


# ---------------------------------------------------------------------------- #
#                              Recommended Company                             #
# ---------------------------------------------------------------------------- #


@admin_required
def recommended_company_admin(request):
    recommended_companys = Recommended_company.objects.all().order_by('id')

    context = {
        'recommended_companys': recommended_companys,

    }

    return render(request, 'recommended_company/recommended_company_admin.html', context)


@admin_required
def recommended_company_create(request):
    if request.method == 'POST':
        form = RecommendedCompanyForm(request.POST, request.FILES)
        if form.is_valid():
            recommended_company = Recommended_company()
            recommended_company.title = form.cleaned_data.get('title')
            recommended_company.description = form.cleaned_data.get(
                'description')
            if request.FILES:
                recommended_company.image = request.FILES['image']
            recommended_company.save()
            messages.success(request, "Malumotlaringiz qoshildi ")
            return redirect('recommended_company_admin')
    form = RecommendedCompanyForm()
    context = {
        'form': form,
    }
    return render(request, 'recommended_company/recommended_company_create.html', context)


@admin_required
def recommended_company_edit(request, id):
    recommended_company = Recommended_company.objects.get(pk=id)
    if request.method == 'POST':
        form = RecommendedCompanyForm(
            request.POST, request.FILES, instance=recommended_company)
        if form.is_valid():
            if request.FILES:
                recommended_company.image = request.FILES['image']
            form.save()
            messages.success(request, "Malumotlaringiz o`zgartirildi")
            return redirect('recommended_company_admin')
    else:
        form = RecommendedCompanyForm(instance=recommended_company)
        context = {'form': form}

        return render(request, 'recommended_company/recommended_company_edit.html', context)


@admin_required
def recommended_company_delate(request, id):
    recommended_company = Recommended_company.objects.get(pk=id)
    recommended_company.delete()
    messages.success(request, "Malumotlaringiz o'chirildi ")
    return redirect('recommended_company_admin')


# ---------------------------------------------------------------------------- #
#                                    License                                   #
# ---------------------------------------------------------------------------- #


@admin_required
def license_admin(request):
    licenses = License.objects.all().order_by('id')

    context = {
        'licenses': licenses,
    }

    return render(request, 'licenses/license_admin.html', context)


@admin_required
def license_create(request):
    license = License()
    InlineFormSet = inlineformset_factory(License, LicImages, form=LicenseForm, fields=(
        'image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = LicenseForm(request.POST, request.FILES,
                           instance=license, prefix='license')
        formset = InlineFormSet(
            request.POST, request.FILES, instance=license, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request, "Malumotlaringiz qoshildi ")
            return redirect('license_admin')

    else:
        form = LicenseForm(instance=license, prefix='license')
        formset = InlineFormSet(instance=license, prefix='images')

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'licenses/license_create.html', context)


@admin_required
def license_edit(request, id):
    license = License.objects.get(pk=id)
    InlineFormSet = inlineformset_factory(License, LicImages, form=LicenseForm, fields=(
        'image',), extra=5, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        form = LicenseForm(request.POST, request.FILES,
                           instance=license, prefix='license')
        formset = InlineFormSet(
            request.POST, request.FILES, instance=license, prefix='images')
        if all([form.is_valid(), formset.is_valid()],):
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request, "Malumotlaringiz o`zgartirildi")
            return redirect('license_admin')

    else:
        form = LicenseForm(instance=license, prefix='license')
        formset = InlineFormSet(instance=license, prefix='images')

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'licenses/license_edit.html', context)


@admin_required
def license_delate(request, id):
    license = License.objects.get(pk=id)
    license.delete()
    messages.success(request, "Malumotlaringiz o'chirildi ")
    return redirect('license_admin')


# ---------------------------------------------------------------------------- #
#                                  Information                                 #
# ---------------------------------------------------------------------------- #


@admin_required
def information_admin(request):
    informations = Informations.objects.all().order_by('id')

    context = {
        'informations': informations,

    }

    return render(request, 'informations/information_admin.html', context)


@admin_required
def information_create(request):
    if request.method == 'POST':
        form = InformationsForm(request.POST, request.FILES)
        if form.is_valid():
            information = Informations()
            information.title = form.cleaned_data.get('title')
            information.keyword = form.cleaned_data.get('keyword')
            information.description = form.cleaned_data.get('description')
            information.country = form.cleaned_data.get('country')
            information.city = form.cleaned_data.get('city')
            information.address = form.cleaned_data.get('address')
            information.phone = form.cleaned_data.get('phone')
            information.fax = form.cleaned_data.get('fax')
            information.email = form.cleaned_data.get('email')
            information.video = form.cleaned_data.get('video')
            information.telegram = form.cleaned_data.get('telegram')
            information.instagram = form.cleaned_data.get('instagram')
            information.facebook = form.cleaned_data.get('facebook')
            information.youtube = form.cleaned_data.get('youtube')
            information.twitter = form.cleaned_data.get('twitter')
            information.linkedin = form.cleaned_data.get('linkedin')
            information.status = form.cleaned_data.get('status')
            if request.FILES:
                information.image = request.FILES['image']
            information.save()
            messages.success(request, "Malumotlaringiz qoshildi ")
            return redirect('information_admin')
    form = InformationsForm()
    context = {
        'form': form,
    }
    return render(request, 'informations/information_create.html', context)


@admin_required
def information_edit(request, id):
    information = Informations.objects.get(pk=id)
    if request.method == 'POST':
        form = InformationsForm(
            request.POST, request.FILES, instance=information)
        if form.is_valid():
            if request.FILES:
                information.image = request.FILES['image']
            form.save()
            messages.success(request, "Malumotlaringiz o`zgartirildi")
            return redirect('information_admin')
    else:
        form = InformationsForm(instance=information)
        context = {'form': form}

        return render(request, 'informations/information_edit.html', context)


@admin_required
def information_delate(request, id):
    information = Informations.objects.get(pk=id)
    information.delete()
    messages.success(request, "Malumotlaringiz o'chirildi ")
    return redirect('information_admin')


# ---------------------------------------------------------------------------- #
#                                Contact Message                               #
# ---------------------------------------------------------------------------- #


@admin_required
def contact_message_admin(request):
    contact_message = ContactMessage.objects.all().order_by('id')

    context = {
        'contact_message': contact_message,

    }

    return render(request, 'contact_message/contact_message_admin.html', context)


@admin_required
def contact_message_detail(request, id):
    contact_message = ContactMessage.objects.get(pk=id)

    context = {
        'contact_message': contact_message,

    }

    return render(request, 'contact_message/contact_message_detail.html', context)


@admin_required
def contact_message_delate(request, id):
    contact_message = ContactMessage.objects.get(pk=id)
    contact_message.delete()
    messages.success(request, "Malumotlaringiz o'chirildi ")
    return redirect('contact_message_admin')


# ---------------------------------------------------------------------------- #
#                                  Order Room                                  #
# ---------------------------------------------------------------------------- #


@admin_required
def order_room_admin(request):
    order_room = Order.objects.all().order_by('id')

    context = {
        'order_room': order_room,

    }

    return render(request, 'order_room/order_room_admin.html', context)


@admin_required
def order_room_edit(request, id):
    order_room = Order.objects.get(pk=id)
    if request.method == 'POST':
        form = EditOrderRoomForm(request.POST, instance=order_room)
        if form.is_valid():
            form.save()
            messages.success(request, "Malumotlaringiz o`zgartirildi")
            return redirect('order_room_admin')
    else:
        form = EditOrderRoomForm(instance=order_room)
        context = {'form': form}

        return render(request, 'order_room/order_room_edit.html', context)


@admin_required
def order_room_detail(request, id):
    order_room = Order.objects.get(pk=id)

    context = {
        'order_room': order_room,
    }

    return render(request, 'order_room/order_room_detail.html', context)


@admin_required
def order_room_delate(request, id):
    order_room = Order.objects.get(pk=id)
    order_room.delete()
    messages.success(request, "Malumotlaringiz o'chirildi ")
    return redirect('order_room_admin')


# ---------------------------------------------------------------------------- #
#                              Order Ticket Events                             #
# ---------------------------------------------------------------------------- #


@admin_required
def order_events_admin(request):
    order_events = Offer_events_ticket.objects.all().order_by('id')

    context = {
        'order_events': order_events,

    }

    return render(request, 'order_events/order_events_admin.html', context)


@admin_required
def order_events_edit(request, id):
    order_events = Offer_events_ticket.objects.get(pk=id)
    if request.method == 'POST':
        form = EditEventsOrderForm(request.POST, instance=order_events)
        if form.is_valid():
            form.save()
            messages.success(request, "Malumotlaringiz o`zgartirildi")
            return redirect('order_events_admin')
    else:
        form = EditEventsOrderForm(instance=order_events)
        context = {'form': form}

        return render(request, 'order_events/order_events_edit.html', context)


@admin_required
def order_events_detail(request, id):
    order_events = Offer_events_ticket.objects.get(pk=id)

    context = {
        'order_events': order_events,
    }

    return render(request, 'order_events/order_events_detail.html', context)


@admin_required
def order_events_delate(request, id):
    order_events = Offer_events_ticket.objects.get(pk=id)
    order_events.delete()
    messages.success(request, "Malumotlaringiz o'chirildi ")
    return redirect('order_events_admin')
