from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, FileInput


from blog.models import Blog, Category, Tag
from home.models import FAQ, Informations, License, ContactMessage, AboutUs, Slider
from service.models import (
                            Service, Image_service, Special_offer, Image_offer,
                            Offer_order, Gallery, Category_gallery, Our_Staff,
                            Category_staff, Restaurant_menu, Events,
                            Image_events, Offer_events_ticket, Place, Image_place
                            )

from .models import CustomUser
from room.models import Room, RoomServices, Room_Image



#=================================== USER BO'LIMI =============================================


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




class AddRoomForm(forms.ModelForm):
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






class EditRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ( 'title',  'price',   'description',  'category', 'image', 'status')

class AddRoomServiceForm(forms.ModelForm):
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

class EditRoomServiceForm(forms.ModelForm):
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

class AddRoomSliderForm(forms.ModelForm):
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


class EditRoomSliderForm(forms.ModelForm):
    class Meta:
        model = Room_Image
        fields = ['room', 'image',]
        widgets = {
            'room': forms.Select(attrs={
                'class': "form-control mb-2"}
            ),

            "image" : FileInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'image',
                'placeholder' : 'image'
            }),
        }



#=================================== SLIDER BO'LIMI =============================================

class CreateSlider(forms.ModelForm):
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


class EditSlider(forms.ModelForm):
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






