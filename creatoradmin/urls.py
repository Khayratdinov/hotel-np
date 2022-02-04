from django.urls import path
from creatoradmin import views


urlpatterns = [


    # ---------------------------------------------------------------------------- #
    #                                ADMIN DASHBOARD                               #
    # ---------------------------------------------------------------------------- #


    path('', views.admin_panel, name='admin_home'),



    # ─────────────────────────────────── USER ─────────────────────────────────── #


    path('users_admin/', views.users_admin, name='users_admin'),
    path('user_edit/<int:user_id>/', views.user_edit, name='user_edit'),
    path('user_detail/<int:user_id>/', views.user_detail, name='user_detail'),
    path('user_delete/<int:user_id>/', views.user_delete, name='user_delete'),


    # ─────────────────────────────────── ROOM ─────────────────────────────────── #


    path('rooms/', views.room, name='rooms_admin'),
    path('room_create/', views.room_create, name='room_create'),
    path('room_edit/<int:id>/', views.room_edit, name='room_edit'),
    path('room_delate/<int:id>/', views.room_delate, name='room_delate'),


    # ──────────────────────────────── HOME SLIDER ─────────────────────────────── #


    path('sliders/', views.sliders, name='sliders'),
    path('slider_create/', views.slider_create, name='slider_create'),
    path('slider_edit/<int:id>/', views.slider_edit, name='slider_edit'),
    path('slider_delate/<int:id>/', views.slider_delate, name='slider_delate'),


    # ─────────────────────────────── CATEGORY ROOM ────────────────────────────── #


    path('categories/', views.categories, name='categories'),
    path('category_create/', views.category_create, name='category_create'),
    path('category_edit/<int:id>/', views.category_edit, name='category_edit'),
    path('category_delate/<int:id>/',
         views.category_delate, name='category_delate'),


    # ────────────────────────────── CATEGORIES_BLOG ───────────────────────────── #


    path('categories_blog/', views.categories_blog, name='categories_blog'),
    path('category_blog_create/', views.category_blog_create,
         name='category_blog_create'),
    path('category_blog_edit/<int:id>/',
         views.category_blog_edit, name='category_blog_edit'),
    path('category_blog_delate/<int:id>/',
         views.category_blog_delate, name='category_blog_delate'),


    # ─────────────────────────────────── BLOGS ────────────────────────────────── #


    path('blogs_admin/', views.blogs, name='blogs_admin'),
    path('blog_create/', views.blog_create, name='blog_create'),
    path('blog_edit/<int:id>/', views.blog_edit, name='blog_edit'),
    path('blog_delate/<int:id>/', views.blog_delate, name='blog_delate'),


    # ───────────────────────────────── SERVICES ───────────────────────────────── #


    path('services_admin/', views.services, name='services_admin'),
    path('service_create/', views.service_create, name='service_create'),
    path('service_edit/<int:id>/', views.service_edit, name='service_edit'),
    path('service_delate/<int:id>/', views.service_delate, name='service_delate'),


    # ────────────────────────────────── ABOUTUS ───────────────────────────────── #


    path('aboutus_admin/', views.aboutus_admin, name='aboutus_admin'),
    path('aboutus_create/', views.aboutus_create, name='aboutus_create'),
    path('aboutus_edit/<int:id>/', views.aboutus_edit, name='aboutus_edit'),
    path('aboutus_delate/<int:id>/', views.aboutus_delate, name='aboutus_delate'),


    # ─────────────────────────────── ABOUTUS_IMAGE ────────────────────────────── #


    path('aboutus_image_admin/', views.aboutus_image_admin,
         name='aboutus_image_admin'),
    path('aboutus_image_create/', views.aboutus_image_create,
         name='aboutus_image_create'),
    path('aboutus_image_edit/<int:id>/',
         views.aboutus_image_edit, name='aboutus_image_edit'),
    path('aboutus_image_delate/<int:id>/',
         views.aboutus_image_delate, name='aboutus_image_delate'),


    # ────────────────────────────── ABOUTUS_FEATURE ───────────────────────────── #


    path('aboutus_feature_admin/', views.aboutus_feature_admin,
         name='aboutus_feature_admin'),
    path('aboutus_feature_create/', views.aboutus_feature_create,
         name='aboutus_feature_create'),
    path('aboutus_feature_edit/<int:id>/',
         views.aboutus_feature_edit, name='aboutus_feature_edit'),
    path('aboutus_feature_delate/<int:id>/',
         views.aboutus_feature_delate, name='aboutus_feature_delate'),


    # ───────────────────────────────── BUSINESS ───────────────────────────────── #


    path('business_admin/', views.business_admin, name='business_admin'),
    path('business_create/', views.business_create, name='business_create'),
    path('business_edit/<int:id>/', views.business_edit, name='business_edit'),
    path('business_delate/<int:id>/',
         views.business_delate, name='business_delate'),


    # ──────────────────────────────── RESTAURANT ──────────────────────────────── #


    path('restaurant_admin/', views.restaurant_admin, name='restaurant_admin'),
    path('restaurant_create/', views.restaurant_create, name='restaurant_create'),
    path('restaurant_edit/<int:id>/',
         views.restaurant_edit, name='restaurant_edit'),
    path('restaurant_delate/<int:id>/',
         views.restaurant_delate, name='restaurant_delate'),


    # ────────────────────────────── RESTAURANT_MENU ───────────────────────────── #


    path('restaurant_menu_admin/', views.restaurant_menu_admin,
         name='restaurant_menu_admin'),
    path('restaurant_menu_create/', views.restaurant_menu_create,
         name='restaurant_menu_create'),
    path('restaurant_menu_edit/<int:id>/',
         views.restaurant_menu_edit, name='restaurant_menu_edit'),
    path('restaurant_menu_delate/<int:id>/',
         views.restaurant_menu_delate, name='restaurant_menu_delate'),


    # ──────────────────────────────────── SPA ─────────────────────────────────── #


    path('spa_admin/', views.spa_admin, name='spa_admin'),
    path('spa_create/', views.spa_create, name='spa_create'),
    path('spa_edit/<int:id>/', views.spa_edit, name='spa_edit'),
    path('spa_delate/<int:id>/', views.spa_delate, name='spa_delate'),


    # ────────────────────────────────── FITNESS ───────────────────────────────── #


    path('fitness_admin/', views.fitness_admin, name='fitness_admin'),
    path('fitness_create/', views.fitness_create, name='fitness_create'),
    path('fitness_edit/<int:id>/', views.fitness_edit, name='fitness_edit'),
    path('fitness_delate/<int:id>/', views.fitness_delate, name='fitness_delate'),


    # ─────────────────────────────── SPECIAL_OFFER ────────────────────────────── #


    path('special_offer_admin/', views.special_offer_admin,
         name='special_offer_admin'),
    path('special_offer_create/', views.special_offer_create,
         name='special_offer_create'),
    path('special_offer_edit/<int:id>/',
         views.special_offer_edit, name='special_offer_edit'),
    path('special_offer_delate/<int:id>/',
         views.special_offer_delate, name='special_offer_delate'),


    path('offer_order_admin/', views.offer_order_admin, name='offer_order_admin'),
    path('offer_order_edit/<int:id>/',
         views.offer_order_edit, name='offer_order_edit'),


    # ───────────────────────────── CATEGORY_GALLERY ───────────────────────────── #


    path('category_gallery_admin/', views.category_gallery_admin,
         name='category_gallery_admin'),
    path('category_gallery_create/', views.category_gallery_create,
         name='category_gallery_create'),
    path('category_gallery_edit/<int:id>/',
         views.category_gallery_edit, name='category_gallery_edit'),
    path('category_gallery_delate/<int:id>/',
         views.category_gallery_delate, name='category_gallery_delate'),


    # ────────────────────────────────── GALLERY ───────────────────────────────── #


    path('gallery_admin/', views.gallery_admin, name='gallery_admin'),
    path('gallery_create/', views.gallery_create, name='gallery_create'),
    path('gallery_edit/<int:id>/', views.gallery_edit, name='gallery_edit'),
    path('gallery_delate/<int:id>/', views.gallery_delate, name='gallery_delate'),


    # ────────────────────────────── CATEGORY_STAFF ────────────────────────────── #


    path('category_staff_admin/', views.category_staff_admin,
         name='category_staff_admin'),
    path('category_staff_create/', views.category_staff_create,
         name='category_staff_create'),
    path('category_staff_edit/<int:id>/',
         views.category_staff_edit, name='category_staff_edit'),
    path('category_staff_delate/<int:id>/',
         views.category_staff_delate, name='category_staff_delate'),



    # ───────────────────────────────── OUR_STAFF ──────────────────────────────── #


    path('our_staff_admin/', views.our_staff_admin, name='our_staff_admin'),
    path('our_staff_create/', views.our_staff_create, name='our_staff_create'),
    path('our_staff_edit/<int:id>/', views.our_staff_edit, name='our_staff_edit'),
    path('our_staff_delate/<int:id>/',
         views.our_staff_delate, name='our_staff_delate'),


    # ────────────────────────────────── EVENTS ────────────────────────────────── #


    path('events_admin/', views.events_admin, name='events_admin'),
    path('event_create/', views.event_create, name='event_create'),
    path('event_edit/<int:id>/', views.event_edit, name='event_edit'),
    path('event_delate/<int:id>/', views.event_delate, name='event_delate'),


    # ─────────────────────────────────── PLACE ────────────────────────────────── #


    path('place_admin/', views.place_admin, name='place_admin'),
    path('place_create/', views.place_create, name='place_create'),
    path('place_edit/<int:id>/', views.place_edit, name='place_edit'),
    path('place_delate/<int:id>/', views.place_delate, name='place_delate'),


    # ──────────────────────────────── TESTIMONIAL ─────────────────────────────── #


    path('testimonial_admin/', views.testimonial_admin, name='testimonial_admin'),
    path('testimonial_create/', views.testimonial_create,
         name='testimonial_create'),
    path('testimonial_edit/<int:id>/',
         views.testimonial_edit, name='testimonial_edit'),
    path('testimonial_delate/<int:id>/',
         views.testimonial_delate, name='testimonial_delate'),



    # ──────────────────────────── RECOMMENDED_COMPANY ─────────────────────────── #


    path('recommended_company_admin/', views.recommended_company_admin,
         name='recommended_company_admin'),
    path('recommended_company_create/', views.recommended_company_create,
         name='recommended_company_create'),
    path('recommended_company_edit/<int:id>/',
         views.recommended_company_edit, name='recommended_company_edit'),
    path('recommended_company_delate/<int:id>/',
         views.recommended_company_delate,  name='recommended_company_delate'),


    # ────────────────────────────────── LICENSE ───────────────────────────────── #


    path('license_admin/', views.license_admin, name='license_admin'),
    path('license_create/', views.license_create, name='license_create'),
    path('license_edit/<int:id>/', views.license_edit, name='license_edit'),
    path('license_delate/<int:id>/', views.license_delate, name='license_delate'),


    # ─────────────────────────────── INFORMATIONS ─────────────────────────────── #


    path('information_admin/', views.information_admin, name='information_admin'),
    path('information_create/', views.information_create,
         name='information_create'),
    path('information_edit/<int:id>/',
         views.information_edit, name='information_edit'),
    path('information_delate/<int:id>/',
         views.information_delate, name='information_delate'),


    # ────────────────────────────── CONTACT MESSAGE ───────────────────────────── #


    path('contact_message_admin/', views.contact_message_admin,
         name='contact_message_admin'),
    path('contact_message_detail/<int:id>/',
         views.contact_message_detail, name='contact_message_detail'),
    path('contact_message_delate/<int:id>/',
         views.contact_message_delate, name='contact_message_delate'),


    # ──────────────────────────────── ORDER ROOM ──────────────────────────────── #


    path('order_room_admin/', views.order_room_admin, name='order_room_admin'),
    path('order_room_edit/<int:id>/',
         views.order_room_edit, name='order_room_edit'),
    path('order_room_detail/<int:id>/',
         views.order_room_detail, name='order_room_detail'),
    path('order_room_delate/<int:id>/',
         views.order_room_delate, name='order_room_delate'),


    # ──────────────────────────── ORDER TICKET EVENTS ─────────────────────────── #


    path('order_events_admin/', views.order_events_admin,
         name='order_events_admin'),
    path('order_events_edit/<int:id>/',
         views.order_events_edit, name='order_events_edit'),
    path('order_events_detail/<int:id>/',
         views.order_events_detail, name='order_events_detail'),
    path('order_events_delate/<int:id>/',
         views.order_events_delate, name='order_events_delate'),





















































    # path('logout_form/', views.logout_form, name='logout_form'),
    # path('user_update/', views.user_update, name='user_update'),
    # path('user_password/', views.user_password, name='user_password'),


]
