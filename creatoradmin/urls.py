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



    # path('logout_form/', views.logout_form, name='logout_form'),
    # path('user_update/', views.user_update, name='user_update'),
    # path('user_password/', views.user_password, name='user_password'),


]