from django.urls import path
from creatoradmin import views

urlpatterns = [

    # ====================  USERLARGA TEGISHLI BO'LIM  ====================

    path('register/', views.register_user, name='register'),
    path('login/', views.login_form, name='login_form'),
    path('admin/', views.HomeAminView.as_view(), name='admin_home'),
    
    path('rooms/', views.room, name='rooms_admin'),
    path('room_create/', views.room_create, name='room_create'),
    path('room_edit/<int:id>/', views.room_edit, name = 'room_edit'),
    path('room_delate/<int:id>/', views.room_delate, name = 'room_delate'),


    # ==================== HOME SLIDER BOLIMI ====================

    path('sliders/', views.sliders, name ='sliders'),
    path('slider_create/', views.slider_create, name ='slider_create'),
    path('slider_edit/<int:id>', views.slider_edit, name='slider_edit'),
    path('slider_delate/<int:id>', views.slider_delate, name='slider_delate'),


    # ─── CATEGORY ROOM ──────────────────────────────────────────────────────────────

    path('categories/', views.categories, name ='categories'),
    path('category_create/', views.category_create, name ='category_create'),
    path('category_edit/<int:id>', views.category_edit, name='category_edit'),
    path('category_delate/<int:id>', views.category_delate, name='category_delate'),


    # ─── CATEGORY BLOG ──────────────────────────────────────────────────────────────

    path('categories_blog/', views.categories_blog, name ='categories_blog'),
    path('category_blog_create/', views.category_blog_create, name ='category_blog_create'),
    path('category_blog_edit/<int:id>', views.category_blog_edit, name='category_blog_edit'),
    path('category_blog_delate/<int:id>', views.category_blog_delate, name='category_blog_delate'),


    # ─── BLOG ───────────────────────────────────────────────────────────────────────

    path('blogs/', views.blogs, name ='blogs_admin'),
    path('blog_create/', views.blog_create, name ='blog_create'),
    path('blog_edit/<int:id>', views.blog_edit, name='blog_edit'),
    path('blog_delate/<int:id>', views.blog_delate, name='blog_delate'),


    # ─── SERVICES ───────────────────────────────────────────────────────────────────

    path('services_admin/', views.services, name ='services_admin'),
    path('service_create/', views.service_create, name ='service_create'),
    path('service_edit/<int:id>', views.service_edit, name='service_edit'),
    path('service_delate/<int:id>', views.service_delate, name='service_delate'),


    # ─── ABOUT US ───────────────────────────────────────────────────────────────────

    # path('aboutus_create/', views.aboutus_create, name ='aboutus_create'),
    # path('aboutus_edit/', views.aboutus_edit, name='aboutus_edit'),













    # path('logout_form/', views.logout_form, name='logout_form'),
    # path('user_update/', views.user_update, name='user_update'),
    # path('user_password/', views.user_password, name='user_password'),


]