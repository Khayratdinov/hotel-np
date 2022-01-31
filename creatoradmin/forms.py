from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, FileInput, NumberInput, DateInput


from blog.models import Blog, Category_Blog, Tag_Blog
from home.models import *

from service.models import (
                            Service, Business, Restaurant, Restaurant_menu,
                            Spa, Fitness, Special_offer, Offer_order, Gallery,
                            Category_gallery, Our_Staff, Category_staff, Events,
                            Offer_events_ticket, Place
                            )

from .models import CustomUser
from room.models import Room, RoomServices, Room_Image, Category




#
# ───────────────────────────────────────────────────────────────────── USER ─────
#

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'full_name', 'email', 'phone', 'user_type', 'password1', 'password2', )

        widgets = {
            "username" : TextInput(attrs={
                'class' : 'form-control',
                'id' : 'name',
                'placeholder' : 'Enter your name'
            }),
            "full_name" : TextInput(attrs={
                'class' : 'form-control',
                'id' : 'fullname',
                'placeholder' : 'Enter your name'
            }),
            "email" : EmailInput(attrs={
                'class' : 'form-control',
                'id' : 'emailaddress',
                'placeholder' : 'Enter your email'
            }),
            "phone" : TextInput(attrs={
                'class' : 'form-control',
                'id' : 'phone',
                'placeholder' : 'Enter your phone'
            }),
            "password1" : PasswordInput(attrs={
                'class' : 'form-control',
                'id' : 'password1',
                'placeholder' : 'Enter your password'
            }),
            "password2" : PasswordInput(attrs={
                'class' : 'form-control',
                'id' : 'password2',
                'placeholder' : 'Enter your password'
            }),

            'user_type': forms.Select(attrs={
                'class': "form-control"}
            )
        }

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'full_name', 'phone',)

#
# ───────────────────────────────────────────────────────────────────── ROOM ─────
#

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ( 'title',  'price',   'description', 'text',  'category', 'image', 'status')

        widgets = {
            "title" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'title',
                'placeholder' : 'title'
            }),

            "price" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'price',
                'placeholder' : 'price'
            }),

            "description" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'description',
                'placeholder' : 'description'
            }),

            "text" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'text',
                'placeholder' : 'text'
            }),


            'category': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),

            "image" : FileInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'image',
                'placeholder' : 'image'
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
        fields = ( 'title',  'description',   'icon',)


        widgets = {
            "title" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'title',
                'placeholder' : 'title'
            }),

            "description" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'description',
                'placeholder' : 'description'
            }),

            "icon" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'icon',
                'placeholder' : 'fab fa-apple'
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

                "image" : FileInput(attrs={
                    'class' : 'form-control mb-2',

                }),
            }


#
# ────────────────────────────────────────────────────────────── HOME SLIDER ─────
#
class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ['title','description','image',]


        widgets = {
            "title" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'title',
                'placeholder' : 'title'
            }),

            "description" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'description',
                'placeholder' : 'description'
            }),

            "image" : FileInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'image',
                'placeholder' : 'image'
            }),
        }

#
# ──────────────────────────────────────────────────────────── CATEGORY ROOM ─────
#

class CategoryRoomForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title','description','image', 'status']

        widgets = {
            "title" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'title',
                'placeholder' : 'title'
            }),

            "description" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'description',
                'placeholder' : 'description'
            }),

            "image" : FileInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'image',
                'placeholder' : 'image'
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
        fields = ['title','description','text', 'category','image', 'status',]

        widgets = {
            "title" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'title',
                'placeholder' : 'title'
            }),

            "description" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'description',
                'placeholder' : 'description'
            }),

            "text" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'text',
                'placeholder' : 'text'
            }),


            'category': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),

            "image" : FileInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'image',
                'placeholder' : 'image'
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
            "title" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'title',
                'placeholder' : 'title'
            }),
        }

#
# ───────────────────────────────────────────────────────────────── SERVICES ─────
#

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title','description',  'text', 'image', 'icon']

        widgets = {
            "title" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'title',
                'placeholder' : 'title'
            }),

            "description" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'description',
                'placeholder' : 'description'
            }),

            "text" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'text',
                'placeholder' : 'text'
            }),

            "image" : FileInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'image',
                'placeholder' : 'image'
            }),

            "icon" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'icon',
                'placeholder' : 'icon'
            }),
        }

#
# ───────────────────────────────────────────────────────────────── ABOUT US ─────
#

class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = ['title','description',  'text', 'image',]

        widgets = {
            "title" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'title',
                'placeholder' : 'title'
            }),

            "description" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'description',
                'placeholder' : 'description'
            }),

            "text" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'text',
                'placeholder' : 'text'
            }),

            "image" : FileInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'image',
                'placeholder' : 'image'
            }),

        }

#
# ────────────────────────────────────────────────────────── ABOUT US IMAGES ─────
#

class AboutUsImageForm(forms.ModelForm):
    class Meta:
        model = Image_aboutus
        fields = ['title','description', 'image',]

        widgets = {
            "title" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'title',
                'placeholder' : 'title'
            }),

            "description" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'description',
                'placeholder' : 'description'
            }),

            "image" : FileInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'image',
                'placeholder' : 'image'
            }),

        }

#
# ───────────────────────────────────────────────────────── ABOUT US FEATURE ─────
#

class AboutUsFeatureForm(forms.ModelForm):
    class Meta:
        model = AboutUs_features
        fields = ['name','number', 'icon', 'image',]

        widgets = {
            "name" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'name',
                'placeholder' : 'name'
            }),

            "number" : NumberInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'number',
                'placeholder' : 'number'
            }),

            "icon" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'icon',
                'placeholder' : 'icon'
            }),

            "image" : FileInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'image',
                'placeholder' : 'image'
            }),

        }

#
# ───────────────────────────────────────────────────────────────── BUSINESS ─────
#

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['title','description', 'text', 'icon', 'image',]

        widgets = {
            "title" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'title',
                'placeholder' : 'title'
            }),

            "description" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'description',
                'placeholder' : 'description'
            }),

            "text" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'text',
                'placeholder' : 'text'
            }),

            "icon" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'icon',
                'placeholder' : 'icon'
            }),

            "image" : FileInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'image',
                'placeholder' : 'image'
            }),

        }



#
# ─────────────────────────────────────────────────────────────── RESTAURANT ─────
#


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['title','description', 'text', 'icon', 'image',]

        widgets = {
            "title" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'title',
                'placeholder' : 'title'
            }),

            "description" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'description',
                'placeholder' : 'description'
            }),

            "text" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'text',
                'placeholder' : 'text'
            }),

            "icon" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'icon',
                'placeholder' : 'icon'
            }),

            "image" : FileInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'image',
                'placeholder' : 'image'
            }),

        }




#
# ────────────────────────────────────────────────────────── RESTAURANT MENU ─────
#

class RestaurantMenuForm(forms.ModelForm):
    class Meta:
        model = Restaurant_menu
        fields = ['title', 'description', 'price', 'status', 'image',]

        widgets = {
            "title" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'title',
                'placeholder' : 'title'
            }),

            "description" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'description',
                'placeholder' : 'description'
            }),

            "price" : NumberInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'price',
                'placeholder' : 'price'
            }),

            

            'status': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),

            "image" : FileInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'image',
                'placeholder' : 'image'
            }),

        }



#
# ────────────────────────────────────────────────────────────────────── SPA ─────
#

class SpaForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['title','description', 'text', 'icon', 'image',]

        widgets = {
            "title" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'title',
                'placeholder' : 'title'
            }),

            "description" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'description',
                'placeholder' : 'description'
            }),

            "text" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'text',
                'placeholder' : 'text'
            }),

            "icon" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'icon',
                'placeholder' : 'icon'
            }),

            "image" : FileInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'image',
                'placeholder' : 'image'
            }),

        }



#
# ────────────────────────────────────────────────────────────────── FITNESS ─────
#


class FitnessForm(forms.ModelForm):
    class Meta:
        model = Fitness
        fields = ['title','description', 'text', 'icon', 'image',]

        widgets = {
            "title" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'title',
                'placeholder' : 'title'
            }),

            "description" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'description',
                'placeholder' : 'description'
            }),

            "text" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'text',
                'placeholder' : 'text'
            }),

            "icon" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'icon',
                'placeholder' : 'icon'
            }),

            "image" : FileInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'image',
                'placeholder' : 'image'
            }),

        }



#
# ──────────────────────────────────────────────────────────── SPECIAL OFFER ─────
#


class SpecialOfferForm(forms.ModelForm):
    class Meta:
        model = Special_offer
        fields = ['title','description', 'text', 'price', 'hot_offer', 'status',  'image',]

        widgets = {
            "title" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'title',
                'placeholder' : 'title'
            }),

            "description" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'description',
                'placeholder' : 'description'
            }),

            "text" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'text',
                'placeholder' : 'text'
            }),

            "price" : NumberInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'price',
                'placeholder' : 'price'
            }),

            'hot_offer': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),

            'status': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),



            "image" : FileInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'image',
                'placeholder' : 'image'
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
            "surname" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'surname',
                'placeholder' : 'surname'
            }),

            "email" : EmailInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'email',
                'placeholder' : 'email'
            }),

            'status': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),

            "date" : DateInput(attrs={
                'class' : 'form-control mb-2 datepicker',
                'id' : 'date',
                'placeholder' : 'date',
                'name' : 'booking-date',
                'readonly' : 'readonly',
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
            "title" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'title',
                'placeholder' : 'title'
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
            "title" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'title',
                'placeholder' : 'title'
            }),

            "image" : FileInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'image',
                'placeholder' : 'image'
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
            "title" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'title',
                'placeholder' : 'title'
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
        fields = ('name', 'surename', 'phone', 'description', 'profession', 'category', 'status', 'image', 'telegram', 'instagram', 'facebook')

        widgets = {
            "name" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'name',
                'placeholder' : 'name'
            }),

            "surename" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'surename',
                'placeholder' : 'surename'
            }),

            "phone" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'phone',
                'placeholder' : 'phone'
            }),

            "profession" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'profession',
                'placeholder' : 'profession'
            }),

            "description" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'description',
                'placeholder' : 'description'
            }),

            'category': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),

            

            'status': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),

            "image" : FileInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'image',
                'placeholder' : 'image'
            }),

            "telegram" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'telegram',
                'placeholder' : 'telegram'
            }),

            "instagram" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'instagram',
                'placeholder' : 'instagram'
            }),

            "facebook" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'facebook',
                'placeholder' : 'facebook'
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
            "title" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'title',
                'placeholder' : 'title'
            }),

            "description" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'description',
                'placeholder' : 'description'
            }),

            "text" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'text',
                'placeholder' : 'text'
            }),

            "date" : DateInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'date',
                'placeholder' : 'date'
            }),

            "image" : FileInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'image',
                'placeholder' : 'image'
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
            "title" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'title',
                'placeholder' : 'title'
            }),

            "description" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'description',
                'placeholder' : 'description'
            }),

            "text" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'text',
                'placeholder' : 'text'
            }),



            "image" : FileInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'image',
                'placeholder' : 'image'
            }),

            'status': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),

        }

