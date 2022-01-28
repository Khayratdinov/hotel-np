from django.contrib import admin
from blog.models import Blog, Category_Blog, Tag_Blog, Comment_blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title',  'image',  'status', 'create_at',]

class CategoryBlogAdmin(admin.ModelAdmin):
    list_display = ['title',]

class TagBlogAdmin(admin.ModelAdmin):
    list_display = ['title',]


class Comment_blogAdmin(admin.ModelAdmin):
    list_display = [ 'comment', 'status',]
    list_filter = ['status']
    readonly_fields = ( 'comment', 'ip',  'blog',)



admin.site.register(Blog, BlogAdmin)
admin.site.register(Category_Blog, CategoryBlogAdmin)
admin.site.register(Tag_Blog, TagBlogAdmin)
admin.site.register(Comment_blog, Comment_blogAdmin)