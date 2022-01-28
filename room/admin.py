from django.contrib import admin
from room.models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title',  'status',]


class RoomImageInline(admin.TabularInline): 
    model = Room_Image
    extra = 5 

class RoomServicesInline(admin.TabularInline):
    model = RoomServices
 
class RoomsAdmin(admin.ModelAdmin): 
    list_display = ['category','title','price', 'status','image_tag',]
    list_filter = ['category',]
    readonly_fields = ('image_tag',) 
    inlines = [RoomImageInline, RoomServicesInline]
    prepopulated_fields = {'slug':('title',)}








admin.site.register(Category,CategoryAdmin)
admin.site.register(Room,RoomsAdmin)
admin.site.register(Comment)
admin.site.register(Room_Image,)
admin.site.register(Order)
