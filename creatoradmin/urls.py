from django.urls import path
from creatoradmin import views

urlpatterns = [


    # ─── USER ───────────────────────────────────────────────────────────────────────


    path('register/', views.register_user, name='register'),
    path('login/', views.login_form, name='login_form'),
    path('admin/', views.HomeAminView.as_view(), name='admin_home'),
    

    # ─── ROOM ───────────────────────────────────────────────────────────────────────


    path('rooms/', views.room, name='rooms_admin'),
    path('room_create/', views.room_create, name='room_create'),
    path('room_edit/<int:id>/', views.room_edit, name = 'room_edit'),
    path('room_delate/<int:id>/', views.room_delate, name = 'room_delate'),


    # ─── HOME SLIDER ────────────────────────────────────────────────────────────────


    path('sliders/', views.sliders, name ='sliders'),
    path('slider_create/', views.slider_create, name ='slider_create'),
    path('slider_edit/<int:id>/', views.slider_edit, name='slider_edit'),
    path('slider_delate/<int:id>/', views.slider_delate, name='slider_delate'),


    # ─── CATEGORY ROOM ──────────────────────────────────────────────────────────────


    path('categories/', views.categories, name ='categories'),
    path('category_create/', views.category_create, name ='category_create'),
    path('category_edit/<int:id>/', views.category_edit, name='category_edit'),
    path('category_delate/<int:id>/', views.category_delate, name='category_delate'),


    # ─── CATEGORY BLOG ──────────────────────────────────────────────────────────────


    path('categories_blog/', views.categories_blog, name ='categories_blog'),
    path('category_blog_create/', views.category_blog_create, name ='category_blog_create'),
    path('category_blog_edit/<int:id>/', views.category_blog_edit, name='category_blog_edit'),
    path('category_blog_delate/<int:id>/', views.category_blog_delate, name='category_blog_delate'),


    # ─── BLOG ───────────────────────────────────────────────────────────────────────


    path('blogs_admin/', views.blogs, name ='blogs_admin'),
    path('blog_create/', views.blog_create, name ='blog_create'),
    path('blog_edit/<int:id>/', views.blog_edit, name='blog_edit'),
    path('blog_delate/<int:id>/', views.blog_delate, name='blog_delate'),


    # ─── SERVICES ───────────────────────────────────────────────────────────────────


    path('services_admin/', views.services, name ='services_admin'),
    path('service_create/', views.service_create, name ='service_create'),
    path('service_edit/<int:id>/', views.service_edit, name='service_edit'),
    path('service_delate/<int:id>/', views.service_delate, name='service_delate'),


    # ─── ABOUT US ───────────────────────────────────────────────────────────────────


    path('aboutus_admin/', views.aboutus_admin, name ='aboutus_admin'),
    path('aboutus_create/', views.aboutus_create, name ='aboutus_create'),
    path('aboutus_edit/<int:id>/', views.aboutus_edit, name='aboutus_edit'),
    path('aboutus_delate/<int:id>/', views.aboutus_delate, name='aboutus_delate'),


    # ─── ABOUT US IMAGES ────────────────────────────────────────────────────────────


    path('aboutus_image_admin/', views.aboutus_image_admin, name ='aboutus_image_admin'),
    path('aboutus_image_create/', views.aboutus_image_create, name ='aboutus_image_create'),
    path('aboutus_image_edit/<int:id>/', views.aboutus_image_edit, name='aboutus_image_edit'),
    path('aboutus_image_delate/<int:id>/', views.aboutus_image_delate, name='aboutus_image_delate'),


    # ─── ABOUT US FEATURES ──────────────────────────────────────────────────────────


    path('aboutus_feature_admin/', views.aboutus_feature_admin, name ='aboutus_feature_admin'),
    path('aboutus_feature_create/', views.aboutus_feature_create, name ='aboutus_feature_create'),
    path('aboutus_feature_edit/<int:id>/', views.aboutus_feature_edit, name='aboutus_feature_edit'),
    path('aboutus_feature_delate/<int:id>/', views.aboutus_feature_delate, name='aboutus_feature_delate'),


    # ─── BUSINESS ───────────────────────────────────────────────────────────────────


    path('business_admin/', views.business_admin, name ='business_admin'),
    path('business_create/', views.business_create, name ='business_create'),
    path('business_edit/<int:id>/', views.business_edit, name='business_edit'),
    path('business_delate/<int:id>/', views.business_delate, name='business_delate'),


    # ─── RESTAURANT ─────────────────────────────────────────────────────────────────


    path('restaurant_admin/', views.restaurant_admin, name ='restaurant_admin'),
    path('restaurant_create/', views.restaurant_create, name ='restaurant_create'),
    path('restaurant_edit/<int:id>/', views.restaurant_edit, name='restaurant_edit'),
    path('restaurant_delate/<int:id>/', views.restaurant_delate, name='restaurant_delate'),


    # ─── RESTAURANT MENU ────────────────────────────────────────────────────────────


    path('restaurant_menu_admin/', views.restaurant_menu_admin, name ='restaurant_menu_admin'),
    path('restaurant_menu_create/', views.restaurant_menu_create, name ='restaurant_menu_create'),
    path('restaurant_menu_edit/<int:id>/', views.restaurant_menu_edit, name='restaurant_menu_edit'),
    path('restaurant_menu_delate/<int:id>/', views.restaurant_menu_delate, name='restaurant_menu_delate'),


    # ─── SPA ────────────────────────────────────────────────────────────────────────


    path('spa_admin/', views.spa_admin, name ='spa_admin'),
    path('spa_create/', views.spa_create, name ='spa_create'),
    path('spa_edit/<int:id>/', views.spa_edit, name='spa_edit'),
    path('spa_delate/<int:id>/', views.spa_delate, name='spa_delate'),


    # ─── FITNESS ────────────────────────────────────────────────────────────────────


    path('fitness_admin/', views.fitness_admin, name ='fitness_admin'),
    path('fitness_create/', views.fitness_create, name ='fitness_create'),
    path('fitness_edit/<int:id>/', views.fitness_edit, name='fitness_edit'),
    path('fitness_delate/<int:id>/', views.fitness_delate, name='fitness_delate'),


    # ─── SPECIAL OFFER ──────────────────────────────────────────────────────────────


    path('special_offer_admin/', views.special_offer_admin, name ='special_offer_admin'),
    path('special_offer_create/', views.special_offer_create, name ='special_offer_create'),
    path('special_offer_edit/<int:id>/', views.special_offer_edit, name='special_offer_edit'),
    path('special_offer_delate/<int:id>/', views.special_offer_delate, name='special_offer_delate'),

    
    path('offer_order_admin/', views.offer_order_admin, name='offer_order_admin'),
    path('offer_order_edit/<int:id>/', views.offer_order_edit, name ='offer_order_edit'),


    # ─── CATEGORY GALLERY ───────────────────────────────────────────────────────────


    path('category_gallery_admin/', views.category_gallery_admin, name ='category_gallery_admin'),
    path('category_gallery_create/', views.category_gallery_create, name ='category_gallery_create'),
    path('category_gallery_edit/<int:id>/', views.category_gallery_edit, name='category_gallery_edit'),
    path('category_gallery_delate/<int:id>/', views.category_gallery_delate, name='category_gallery_delate'),


    # ─── GALLERY ────────────────────────────────────────────────────────────────────


    path('gallery_admin/', views.gallery_admin, name ='gallery_admin'),
    path('gallery_create/', views.gallery_create, name ='gallery_create'),
    path('gallery_edit/<int:id>/', views.gallery_edit, name='gallery_edit'),
    path('gallery_delate/<int:id>/', views.gallery_delate, name='gallery_delate'),


    # ─── CATEGORY STAFF ─────────────────────────────────────────────────────────────


    path('category_staff_admin/', views.category_staff_admin, name ='category_staff_admin'),
    path('category_staff_create/', views.category_staff_create, name ='category_staff_create'),
    path('category_staff_edit/<int:id>/', views.category_staff_edit, name='category_staff_edit'),
    path('category_staff_delate/<int:id>/', views.category_staff_delate, name='category_staff_delate'),



    # ─── OUR STAFF ──────────────────────────────────────────────────────────────────


    path('our_staff_admin/', views.our_staff_admin, name ='our_staff_admin'),
    path('our_staff_create/', views.our_staff_create, name ='our_staff_create'),
    path('our_staff_edit/<int:id>/', views.our_staff_edit, name='our_staff_edit'),
    path('our_staff_delate/<int:id>/', views.our_staff_delate, name='our_staff_delate'),


    # ─── EVENTS ─────────────────────────────────────────────────────────────────────


    path('events_admin/', views.events_admin, name ='events_admin'),
    path('event_create/', views.event_create, name ='event_create'),
    path('event_edit/<int:id>/', views.event_edit, name='event_edit'),
    path('event_delate/<int:id>/', views.event_delate, name='event_delate'),


    # ─── PLACE ──────────────────────────────────────────────────────────────────────


    path('place_admin/', views.place_admin, name ='place_admin'),
    path('place_create/', views.place_create, name ='place_create'),
    path('place_edit/<int:id>/', views.place_edit, name='place_edit'),
    path('place_delate/<int:id>/', views.place_delate, name='place_delate'),








































    # path('logout_form/', views.logout_form, name='logout_form'),
    # path('user_update/', views.user_update, name='user_update'),
    # path('user_password/', views.user_password, name='user_password'),


]