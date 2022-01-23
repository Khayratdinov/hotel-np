from django.contrib import admin
from home.models import Informations, License, LicImages, ContactMessage, FAQ, AboutUs, Slider

class InformationsAdmin(admin.ModelAdmin):
    list_display = ['title', 'country', 'city', 'address', 'phone', 'status', 'create_at',]

class LicenseImageInline(admin.TabularInline):
    model = LicImages
    extra = 5

class LicenseAdmin(admin.ModelAdmin):
    list_display = ['title','image_tag']
    list_filter = ['title']
    readonly_fields = ('image_tag',)
    inlines = [LicenseImageInline]

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'phone', 'email', 'message', 'creat_at',]
    readonly_fields = ('name', 'subject', 'phone', 'email', 'message', 'ip','creat_at',)
    list_filter = ['status']


class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'ordernumber', 'status']
    list_filter = ['status']

class AboutusAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']



admin.site.register(Informations, InformationsAdmin)
admin.site.register(License, LicenseAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(AboutUs, AboutusAdmin)
admin.site.register(Slider, SliderAdmin)

