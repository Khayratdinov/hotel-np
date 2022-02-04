from django.urls import path
from accounts import views


urlpatterns = [


    # ───────────────────────── USER REGISTER AND PROFILE ──────────────────────── #


    path('register/', views.register_user, name='register'),
    path('login/', views.login_form, name='login_form'),
    path('logout_form/', views.logout_form, name='logout_form'),
    path('profile/', views.profile, name='profile'),
    path('profile_edit/<int:id>/', views.profile_edit, name='profile_edit'),


    # ---------------------------------------------------------------------------- #



]
