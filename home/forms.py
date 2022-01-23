from django import forms
from home.models import ContactMessage
from room.models import Order


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
    catid = forms.IntegerField()


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ( 'name','surname','phone', 'citizenship', 'category', 'select', 'pay', 'email','guest', 'arrival', 'departure','room',)


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ( 'name','email', 'phone', 'subject', 'message',)