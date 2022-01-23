from django.urls import path
from blog import views


urlpatterns = [
    path('', views.blog,name='blog'),
    path('blog/<int:id>', views.blog_detail, name='blog_detail'),
    path('comment_blog/<int:id>', views.comment_blog, name='comment_blog'),
]