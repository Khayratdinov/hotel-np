from django.urls import path
from blog import views


urlpatterns = [

    # ─────────────────────────────────── BLOG ─────────────────────────────────── #

    path('', views.blog, name='blog'),
    path('blog/<int:blog_id>', views.blog_detail, name='blog_detail'),
    path('comment_blog/<int:blog_id>', views.comment_blog, name='comment_blog'),


    # ---------------------------------------------------------------------------- #
]
