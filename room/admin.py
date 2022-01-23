from django.contrib import admin
from room.models import *
from mptt.admin import DraggableMPTTAdmin

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'status',]
    list_display_links = ('indented_title',)

class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions','indented_title','related_rooms_page_count','related_rooms_page_cumulative_count',)
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug':('title',)} 

    def get_queryset(self,request):
        qs = super().get_queryset(request)

        qs = Category.objects.add_related_count( 
            qs,
            Room,
            'category',
            'rooms_page_cumulative_count',
            cumulative=True
        )

        qs = Category.objects.add_related_count(
            qs,
            Room,
            'category',
            'rooms_page_count',
            cumulative=False
        )
        return qs

    def related_rooms_page_count(self,instance): 
        return instance.rooms_page_count
    related_rooms_page_count.short_description = 'Related rooms_page (for this specific category)'

    def related_rooms_page_cumulative_count(self,instance): 
        return instance.rooms_page_cumulative_count
    related_rooms_page_cumulative_count.short_description = 'Related rooms_page (in tree)'

class RoomImageInline(admin.TabularInline): 
    model = Image
    extra = 5 

class RoomServicesInline(admin.TabularInline):
    model = RoomServices
 
class RoomsAdmin(admin.ModelAdmin): # Xonaning ozi
    list_display = ['category','title','price', 'status','image_tag',]
    list_filter = ['category',]
    readonly_fields = ('image_tag',) # doyimiy ravshda oqishi
    inlines = [RoomImageInline, RoomServicesInline]
    prepopulated_fields = {'slug':('title',)}



class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','phone','comment','status',]
    list_filter = ['status',]
    readonly_fields = ('name','phone','comment','ip','room','rate',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['name','surname','phone','citizenship','pay','email','guest','arrival','departure','room','category','ip',]
    list_filter = ['status',]





admin.site.register(Category,CategoryAdmin2)
admin.site.register(Room,RoomsAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Image,)
admin.site.register(Order,OrderAdmin)
