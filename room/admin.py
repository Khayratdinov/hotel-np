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



class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','phone','comment','status',]
    list_filter = ['status',]
    readonly_fields = ('name','phone','comment','ip','room','rate',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['name','surname','phone','citizenship','pay','email','guest','arrival','departure','room','category','ip',]
    list_filter = ['status',]





admin.site.register(Category,CategoryAdmin)
admin.site.register(Room,RoomsAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Room_Image,)
admin.site.register(Order,OrderAdmin)
