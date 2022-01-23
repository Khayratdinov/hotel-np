from django.contrib import admin
from service.models import (Service, Image_service,  Special_offer, Image_offer,  Offer_order,
                            Gallery, Category_gallery, Our_Staff, Category_staff, Restaurant_menu,
                            Events, Image_events, Offer_events_ticket,  Place, Image_place,
                            )

# Register your models here.
class ImageServiceInline(admin.TabularInline): 
    model = Image_service
    extra = 5 

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    inlines = [ImageServiceInline]

class ImageOfferInline(admin.TabularInline): 
    model = Image_offer
    extra = 5 

class Special_offerAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'hot_offer', 'status']
    inlines = [ImageOfferInline]

class Offer_orderAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone', 'date', 'select', 'status']

class CategoryGalleryAdmin(admin.ModelAdmin):
    list_display = ['title']

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title',]

class CategoryStaffAdmin(admin.ModelAdmin):
    list_display = ['title']

class Our_StaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'surename', 'profession', 'status']

class Restaurant_menuAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'status']

class ImageEventsInline(admin.TabularInline): 
    model = Image_events
    extra = 5 

class EventsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    inlines = [ImageEventsInline]

class OfferEventsTicketAdmin(admin.ModelAdmin):
    list_display = ['name', 'status'] 

class ImagePlaceInline(admin.TabularInline): 
    model = Image_place
    extra = 5 

class PlaceAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    inlines = [ImagePlaceInline]

admin.site.register(Service, ServiceAdmin,)
admin.site.register(Special_offer, Special_offerAdmin)
admin.site.register(Offer_order, Offer_orderAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Category_gallery, CategoryGalleryAdmin)
admin.site.register(Our_Staff, Our_StaffAdmin)
admin.site.register(Category_staff, CategoryStaffAdmin)
admin.site.register(Restaurant_menu, Restaurant_menuAdmin)
admin.site.register(Events, EventsAdmin)
admin.site.register(Offer_events_ticket, OfferEventsTicketAdmin)
admin.site.register(Place, PlaceAdmin)