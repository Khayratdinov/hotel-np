from django.urls import path
from room import views

urlpatterns = [


    path('addcommetn/<int:room_id>',views.addcomment,name='addcomment'),
    path('rooms/', views.rooms, name='rooms'),
    path('room_detail/<int:room_id>', views.room_detail, name='room_detail'),

    
]