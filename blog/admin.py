from django.contrib import admin
from blog.models import Blog, Category, Tag, Comment_blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title',  'image',  'status', 'create_at',]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title',]

class TagAdmin(admin.ModelAdmin):
    list_display = ['title',]


class Comment_blogAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone', 'comment', 'status',]
    list_filter = ['status']
    readonly_fields = ('name', 'surname', 'phone', 'comment', 'ip',  'blog',)



admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment_blog, Comment_blogAdmin)