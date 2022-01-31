from django import forms
from home.models import ContactMessage
from room.models import Order
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, FileInput, DateInput
from service.models import Special_offer, Offer_order


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
    catid = forms.IntegerField()


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ( 'name', 'phone', 'citizenship', 'category',  'pay', 'email','guest', 'arrival', 'departure','room',)

class HomeOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ( 'name', 'phone', 'room', 'arrival', 'departure', 'guest',)

        widgets = {
            "name" : TextInput(attrs={
                'class' : 'form-control',
                'id' : 'name',
                'placeholder' : 'Enter your name'
            }),

            "phone" : TextInput(attrs={
                'class' : 'form-control',
                'id' : 'phone',
                'placeholder' : 'Enter your phone'
            }),

            'room': forms.Select(attrs={
                'class': "form-control"}
            )
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ( 'name','email', 'phone', 'subject', 'message',)


#
# ────────────────────────────────────────────────────── SPECIAL OFFER ORDER ─────
#


class SpecialOfferForm(forms.ModelForm):
    class Meta:
        model = Offer_order
        fields = ['name','phone', 'date', 'text']

        widgets = {
            "name" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'name',
                'placeholder' : 'name'
            }),

            "phone" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'phone',
                'placeholder' : 'phone'
            }),

            "date" : DateInput(attrs={
                'class' : 'form-control mb-2 datepicker',
                'id' : 'date',
                'placeholder' : 'date',
                'name' : 'booking-date',
                'readonly' : 'readonly',
            }),

            "text" : TextInput(attrs={
                'class' : 'form-control mb-2',
                'id' : 'text',
                'placeholder' : 'text'
            }),

        }