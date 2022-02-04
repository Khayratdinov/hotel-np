from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, FileInput, NumberInput, DateInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import CustomUser


from blog.models import Blog, Category_Blog, Tag_Blog
from home.models import *
from service.models import (
    Service, Business, Restaurant, Restaurant_menu,
    Spa, Fitness, Special_offer, Offer_order, Gallery,
    Category_gallery, Our_Staff, Category_staff, Events,
    Offer_events_ticket, Place
)

from room.models import Order, Room, RoomServices, Room_Image, Category


# ───────────────────────────────── USER TYPE ──────────────────────────────── #


class UserTypeChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('avatar',  'user_type',)


#
# ───────────────────────────────────────────────────────────────────── ROOM ─────
#

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('title',  'price',   'description',
                  'text',  'category', 'image', 'status')

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'title',
                'placeholder': 'title'
            }),

            "price": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'price',
                'placeholder': 'price'
            }),

            "description": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'description',
                'placeholder': 'description'
            }),

            "text": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'text',
                'placeholder': 'text'
            }),


            'category': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),

            "image": FileInput(attrs={
                'class': 'form-control mb-2',
                'id': 'image',
                'placeholder': 'image'
            }),

            'status': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),

        }

#
# ───────────────────────────────────────────────────────────── ROOM SERVICE ─────
#


class RoomServiceForm(forms.ModelForm):
    class Meta:
        model = RoomServices
        fields = ('title',  'description',   'icon',)

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'title',
                'placeholder': 'title'
            }),

            "description": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'description',
                'placeholder': 'description'
            }),

            "icon": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'icon',
                'placeholder': 'fab fa-apple'
            }),
        }

#
# ────────────────────────────────────────────────────────────── ROOM SLIDER ─────
#


class RoomSliderForm(forms.ModelForm):
    class Meta:
        model = Room_Image
        fields = ('room', 'image',)

        widgets = {

            'room': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),

            "image": FileInput(attrs={
                'class': 'form-control mb-2',

            }),
        }


#
# ────────────────────────────────────────────────────────────── HOME SLIDER ─────
#
class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ['title', 'description', 'image', ]

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'title',
                'placeholder': 'title'
            }),

            "description": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'description',
                'placeholder': 'description'
            }),

            "image": FileInput(attrs={
                'class': 'form-control mb-2',
                'id': 'image',
                'placeholder': 'image'
            }),
        }

#
# ──────────────────────────────────────────────────────────── CATEGORY ROOM ─────
#


class CategoryRoomForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description', 'image', 'status']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'title',
                'placeholder': 'title'
            }),

            "description": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'description',
                'placeholder': 'description'
            }),

            "image": FileInput(attrs={
                'class': 'form-control mb-2',
                'id': 'image',
                'placeholder': 'image'
            }),

            'status': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),
        }


# ───────────────────────────────── BLOG TAGS ──────────────────────────────── #

class CategoryRoomForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description', 'image', 'status']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'title',
                'placeholder': 'title'
            }),

            "description": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'description',
                'placeholder': 'description'
            }),

            "image": FileInput(attrs={
                'class': 'form-control mb-2',
                'id': 'image',
                'placeholder': 'image'
            }),

            'status': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),
        }

#
# ───────────────────────────────────────────────────────────────────── BLOG ─────
#


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'text',
                  'category', 'image', 'status', ]

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'title',
                'placeholder': 'title'
            }),

            "description": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'description',
                'placeholder': 'description'
            }),

            "text": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'text',
                'placeholder': 'text'
            }),


            'category': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),

            "image": FileInput(attrs={
                'class': 'form-control mb-2',
                'id': 'image',
                'placeholder': 'image'
            }),

            'status': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),
        }

#
# ──────────────────────────────────────────────────────────── CATEGORY BLOG ─────
#


class CategoryBlogForm(forms.ModelForm):
    class Meta:
        model = Category_Blog
        fields = ('title',)

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'title',
                'placeholder': 'title'
            }),
        }

#
# ───────────────────────────────────────────────────────────────── SERVICES ─────
#


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description',  'text', 'image', 'icon']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'title',
                'placeholder': 'title'
            }),

            "description": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'description',
                'placeholder': 'description'
            }),

            "text": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'text',
                'placeholder': 'text'
            }),

            "image": FileInput(attrs={
                'class': 'form-control mb-2',
                'id': 'image',
                'placeholder': 'image'
            }),

            "icon": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'icon',
                'placeholder': 'icon'
            }),
        }

#
# ───────────────────────────────────────────────────────────────── ABOUT US ─────
#


class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = ['title', 'description',  'text', 'image', ]

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'title',
                'placeholder': 'title'
            }),

            "description": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'description',
                'placeholder': 'description'
            }),

            "text": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'text',
                'placeholder': 'text'
            }),

            "image": FileInput(attrs={
                'class': 'form-control mb-2',
                'id': 'image',
                'placeholder': 'image'
            }),

        }

#
# ────────────────────────────────────────────────────────── ABOUT US IMAGES ─────
#


class AboutUsImageForm(forms.ModelForm):
    class Meta:
        model = Image_aboutus
        fields = ['title', 'description', 'image', ]

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'title',
                'placeholder': 'title'
            }),

            "description": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'description',
                'placeholder': 'description'
            }),

            "image": FileInput(attrs={
                'class': 'form-control mb-2',
                'id': 'image',
                'placeholder': 'image'
            }),

        }

#
# ───────────────────────────────────────────────────────── ABOUT US FEATURE ─────
#


class AboutUsFeatureForm(forms.ModelForm):
    class Meta:
        model = AboutUs_features
        fields = ['name', 'number', 'icon', 'image', ]

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'name',
                'placeholder': 'name'
            }),

            "number": NumberInput(attrs={
                'class': 'form-control mb-2',
                'id': 'number',
                'placeholder': 'number'
            }),

            "icon": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'icon',
                'placeholder': 'icon'
            }),

            "image": FileInput(attrs={
                'class': 'form-control mb-2',
                'id': 'image',
                'placeholder': 'image'
            }),

        }

#
# ───────────────────────────────────────────────────────────────── BUSINESS ─────
#


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['title', 'description', 'text', 'icon', 'image', ]

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'title',
                'placeholder': 'title'
            }),

            "description": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'description',
                'placeholder': 'description'
            }),

            "text": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'text',
                'placeholder': 'text'
            }),

            "icon": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'icon',
                'placeholder': 'icon'
            }),

            "image": FileInput(attrs={
                'class': 'form-control mb-2',
                'id': 'image',
                'placeholder': 'image'
            }),

        }


#
# ─────────────────────────────────────────────────────────────── RESTAURANT ─────
#


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['title', 'description', 'text', 'icon', 'image', ]

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'title',
                'placeholder': 'title'
            }),

            "description": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'description',
                'placeholder': 'description'
            }),

            "text": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'text',
                'placeholder': 'text'
            }),

            "icon": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'icon',
                'placeholder': 'icon'
            }),

            "image": FileInput(attrs={
                'class': 'form-control mb-2',
                'id': 'image',
                'placeholder': 'image'
            }),

        }


#
# ────────────────────────────────────────────────────────── RESTAURANT MENU ─────
#

class RestaurantMenuForm(forms.ModelForm):
    class Meta:
        model = Restaurant_menu
        fields = ['title', 'description', 'price', 'status', 'image', ]

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'title',
                'placeholder': 'title'
            }),

            "description": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'description',
                'placeholder': 'description'
            }),

            "price": NumberInput(attrs={
                'class': 'form-control mb-2',
                'id': 'price',
                'placeholder': 'price'
            }),



            'status': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),

            "image": FileInput(attrs={
                'class': 'form-control mb-2',
                'id': 'image',
                'placeholder': 'image'
            }),

        }


#
# ────────────────────────────────────────────────────────────────────── SPA ─────
#

class SpaForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['title', 'description', 'text', 'icon', 'image', ]

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'title',
                'placeholder': 'title'
            }),

            "description": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'description',
                'placeholder': 'description'
            }),

            "text": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'text',
                'placeholder': 'text'
            }),

            "icon": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'icon',
                'placeholder': 'icon'
            }),

            "image": FileInput(attrs={
                'class': 'form-control mb-2',
                'id': 'image',
                'placeholder': 'image'
            }),

        }


#
# ────────────────────────────────────────────────────────────────── FITNESS ─────
#


class FitnessForm(forms.ModelForm):
    class Meta:
        model = Fitness
        fields = ['title', 'description', 'text', 'icon', 'image', ]

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'title',
                'placeholder': 'title'
            }),

            "description": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'description',
                'placeholder': 'description'
            }),

            "text": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'text',
                'placeholder': 'text'
            }),

            "icon": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'icon',
                'placeholder': 'icon'
            }),

            "image": FileInput(attrs={
                'class': 'form-control mb-2',
                'id': 'image',
                'placeholder': 'image'
            }),

        }


#
# ──────────────────────────────────────────────────────────── SPECIAL OFFER ─────
#


class SpecialOfferForm(forms.ModelForm):
    class Meta:
        model = Special_offer
        fields = ['title', 'description', 'text',
                  'price', 'hot_offer', 'status',  'image', ]

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'title',
                'placeholder': 'title'
            }),

            "description": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'description',
                'placeholder': 'description'
            }),

            "text": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'text',
                'placeholder': 'text'
            }),

            "price": NumberInput(attrs={
                'class': 'form-control mb-2',
                'id': 'price',
                'placeholder': 'price'
            }),

            'hot_offer': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),

            'status': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),



            "image": FileInput(attrs={
                'class': 'form-control mb-2',
                'id': 'image',
                'placeholder': 'image'
            }),

        }


#
# ────────────────────────────────────────────────────── SPECIAL OFFER ORDER ─────
#


class SpecialOfferAdminForm(forms.ModelForm):
    class Meta:
        model = Offer_order
        fields = ['surname', 'email', 'status', 'date']

        widgets = {
            "surname": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'surname',
                'placeholder': 'surname'
            }),

            "email": EmailInput(attrs={
                'class': 'form-control mb-2',
                'id': 'email',
                'placeholder': 'email'
            }),

            'status': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),

            "date": DateInput(attrs={
                'class': 'form-control mb-2 datepicker',
                'id': 'date',
                'placeholder': 'date',
                'name': 'booking-date',
                'readonly': 'readonly',
            }),


        }


#
# ───────────────────────────────────────────────────────── CATEGORY GALLERY ─────
#


class CategoryGalleryForm(forms.ModelForm):
    class Meta:
        model = Category_gallery
        fields = ('title', 'cat_filter')

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'title',
                'placeholder': 'title'
            }),



            'cat_filter': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),
        }


#
# ────────────────────────────────────────────────────────────────── GALLERY ─────
#


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('title', 'image', 'cat_filter', 'category')

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'title',
                'placeholder': 'title'
            }),

            "image": FileInput(attrs={
                'class': 'form-control mb-2',
                'id': 'image',
                'placeholder': 'image'
            }),

            'cat_filter': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),

            'category': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),
        }


#
# ─────────────────────────────────────────────────────────── CATEGORY STAFF ─────
#

class CategoryStaffForm(forms.ModelForm):
    class Meta:
        model = Category_staff
        fields = ('title',  'cat_filter',)

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'title',
                'placeholder': 'title'
            }),

            'cat_filter': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),

        }


#
# ──────────────────────────────────────────────────────────────── OUR STAFF ─────
#


class OurStaffForm(forms.ModelForm):
    class Meta:
        model = Our_Staff
        fields = ('name', 'surename', 'phone', 'description', 'profession',
                  'category', 'status', 'image', 'telegram', 'instagram', 'facebook')

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'name',
                'placeholder': 'name'
            }),

            "surename": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'surename',
                'placeholder': 'surename'
            }),

            "phone": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'phone',
                'placeholder': 'phone'
            }),

            "profession": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'profession',
                'placeholder': 'profession'
            }),

            "description": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'description',
                'placeholder': 'description'
            }),

            'category': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),



            'status': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),

            "image": FileInput(attrs={
                'class': 'form-control mb-2',
                'id': 'image',
                'placeholder': 'image'
            }),

            "telegram": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'telegram',
                'placeholder': 'telegram'
            }),

            "instagram": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'instagram',
                'placeholder': 'instagram'
            }),

            "facebook": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'facebook',
                'placeholder': 'facebook'
            }),

        }


#
# ─────────────────────────────────────────────────────────────────── EVENTS ─────
#


class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('title', 'description', 'text', 'date', 'image',  'status',)

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'title',
                'placeholder': 'title'
            }),

            "description": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'description',
                'placeholder': 'description'
            }),

            "text": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'text',
                'placeholder': 'text'
            }),

            "date": DateInput(attrs={
                'class': 'form-control mb-2',
                'id': 'date',
                'placeholder': 'date'
            }),

            "image": FileInput(attrs={
                'class': 'form-control mb-2',
                'id': 'image',
                'placeholder': 'image'
            }),

            'status': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),

        }


#
# ──────────────────────────────────────────────────────────────────── PLACE ─────
#


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('title', 'description', 'text', 'image',  'status',)

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'title',
                'placeholder': 'title'
            }),

            "description": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'description',
                'placeholder': 'description'
            }),

            "text": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'text',
                'placeholder': 'text'
            }),



            "image": FileInput(attrs={
                'class': 'form-control mb-2',
                'id': 'image',
                'placeholder': 'image'
            }),

            'status': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),

        }


#
# ────────────────────────────────────────────────────────────── TESTIMONIAL ─────
#


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ('name', 'location', 'description',
                  'rating', 'photo',  'status',)

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'name',
                'placeholder': 'name'
            }),

            "location": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'location',
                'placeholder': 'location'
            }),

            "description": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'description',
                'placeholder': 'description'
            }),

            "rating": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'rating',
                'placeholder': 'rating'
            }),



            "photo": FileInput(attrs={
                'class': 'form-control mb-2',
                'id': 'image',
                'placeholder': 'image'
            }),

            'status': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),

        }


#
# ────────────────────────────────────────────────────── RECOMMENDED COMPANY ─────
#


class RecommendedCompanyForm(forms.ModelForm):
    class Meta:
        model = Recommended_company
        fields = ('title', 'description', 'image',)

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'title',
                'placeholder': 'title'
            }),

            "description": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'description',
                'placeholder': 'description'
            }),

            "image": FileInput(attrs={
                'class': 'form-control mb-2',
                'id': 'image',
                'placeholder': 'image'
            }),

        }


#
# ────────────────────────────────────────────────────────────────── LICENSE ─────
#


class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = ('title', 'description', 'detail', 'image',)

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'title',
                'placeholder': 'title'
            }),

            "description": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'description',
                'placeholder': 'description'
            }),

            "detail": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'detail',
                'placeholder': 'detail'
            }),

            "image": FileInput(attrs={
                'class': 'form-control mb-2',
                'id': 'image',
                'placeholder': 'image'
            }),

        }


#
# ───────────────────────────────────────────────────────────── INFORMATIONS ─────
#


class InformationsForm(forms.ModelForm):
    class Meta:
        model = Informations
        fields = ('title', 'keyword', 'description', 'country', 'city', 'address', 'phone', 'fax', 'email',
                  'image', 'video', 'telegram', 'instagram', 'facebook', 'youtube', 'twitter', 'linkedin', 'status')

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'title',
                'placeholder': 'title'
            }),

            "keyword": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'keyword',
                'placeholder': 'keyword'
            }),

            "description": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'description',
                'placeholder': 'description'
            }),

            "city": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'city',
                'placeholder': 'city'
            }),

            "country": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'country',
                'placeholder': 'country'
            }),

            "address": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'address',
                'placeholder': 'address'
            }),

            "phone": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'phone',
                'placeholder': 'phone'
            }),

            "fax": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'fax',
                'placeholder': 'fax'
            }),

            "email": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'email',
                'placeholder': 'email'
            }),

            "video": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'video',
                'placeholder': 'video'
            }),

            "image": FileInput(attrs={
                'class': 'form-control mb-2',
                'id': 'image',
                'placeholder': 'image'
            }),

            "telegram": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'telegram',
                'placeholder': 'telegram'
            }),

            "facebook": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'telegram',
                'placeholder': 'telegram'
            }),

            "instagram": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'telegram',
                'placeholder': 'telegram'
            }),

            "youtube": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'youtube',
                'placeholder': 'youtube'
            }),

            "twitter": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'twitter',
                'placeholder': 'twitter'
            }),

            "linkedin": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'linkedin',
                'placeholder': 'linkedin'
            }),

            'status': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),



        }


#
# ────────────────────────────────────────────────────────── CONTACT MESSAGE ─────
#


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'phone', 'subject', 'message', 'status')

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'name',
                'placeholder': 'name'
            }),

            "email": EmailInput(attrs={
                'class': 'form-control mb-2',
                'id': 'email',
                'placeholder': 'email'
            }),

            "phone": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'phone',
                'placeholder': 'phone'
            }),

            "subject": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'subject',
                'placeholder': 'subject'
            }),

            "message": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'message',
                'placeholder': 'message'
            }),

            'status': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),

        }


# -------------------------------- Order Room -------------------------------- #


class EditOrderRoomForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('surname', 'email', 'citizenship', 'pay', 'guest',
                  'children', 'arrival', 'departure', 'status')

        widgets = {
            "surname": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'surname',
                'placeholder': 'surname'
            }),


            "email": EmailInput(attrs={
                'class': 'form-control mb-2',
                'id': 'email',
                'placeholder': 'email'
            }),


            "citizenship": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'citizenship',
                'placeholder': 'citizenship'
            }),

            "pay": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'pay',
                'placeholder': 'pay'
            }),

            "guest": NumberInput(attrs={
                'class': 'form-control mb-2',
                'id': 'guest',
                'placeholder': 'guest'
            }),

            "children": NumberInput(attrs={
                'class': 'form-control mb-2',
                'id': 'children',
                'placeholder': 'children'
            }),

            "arrival": DateInput(attrs={
                'class': 'form-control mb-2',
                'id': 'arrival',
                'placeholder': 'arrival'
            }),

            "departure": DateInput(attrs={
                'class': 'form-control mb-2',
                'id': 'departure',
                'placeholder': 'kuni / oyi / Yili 01.12.2022'
            }),

            'status': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),

        }


# ---------------------------- Order Ticket Events --------------------------- #


# ------------------------------- Events Order ------------------------------- #


class EditEventsOrderForm(forms.ModelForm):

    class Meta:
        model = Offer_events_ticket
        fields = ['surname', 'email', 'text', 'status']

        widgets = {
            "surname": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'surname',
                'placeholder': 'surname'
            }),

            "email": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'email',
                'placeholder': 'email'
            }),


            "text": TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'text',
                'placeholder': 'text'
            }),

            'status': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),



        }
