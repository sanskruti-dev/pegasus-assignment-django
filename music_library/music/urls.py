from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_folder/', views.create_folder, name='create_folder'),
    path('create_music/', views.create_music, name='create_music'),
    path('update_folder/<int:pk>/', views.update_folder, name='update_folder'),
    path('delete_folder/<int:pk>/', views.delete_folder, name='delete_folder'),
    path('add_music_to_folder/<int:folder_id>/', views.add_music_to_folder, name='add_music_to_folder'),
    path('register/', views.register, name='register'),
    path('favorite_music/<int:music_id>/', views.favorite_music, name='favorite_music'),
    path('accounts/profile/', views.profile, name='profile'),
    path('update_music/<int:pk>/', views.update_music, name='update_music'),
    path('delete_music/<int:pk>/', views.delete_music, name='delete_music'),
]
