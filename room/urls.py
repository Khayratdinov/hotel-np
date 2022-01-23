from django.urls import path
from room import views

urlpatterns = [
    path('addcommetn/<int:id>',views.addcomment,name='addcomment'),
    path('rooms/', views.rooms, name='rooms'),
    path('room/<int:id>', views.room_detail, name='room_detail'),
]