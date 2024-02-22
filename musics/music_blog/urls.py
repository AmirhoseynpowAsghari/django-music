from django.urls import path
from .views import AddMusicView, MusicListView, DeleteMusicView, MusicInfoView


urlpatterns = [
    path('', MusicListView.as_view(), name='music_list'),
    path('info/', MusicInfoView.as_view(), name='music_info'),
    path('add_music/', AddMusicView.as_view(), name='add_music'),
    path('delete/<str:pk>/', DeleteMusicView.as_view(), name='delete_music'),
]
