from django.urls import path

from Basic_CRUD_exam.main.views import home_page, album_add, album_details, album_edit, album_delete, \
    profile_page, profile_delete, create_profile

urlpatterns = (
    path('', home_page, name='home page'),
    path('album/add/', album_add, name='add album page'),
    path('album/details/<int:pk>/', album_details, name='album details page'),
    path('album/edit/<int:pk>/', album_edit, name='album edit page'),
    path('album/delete/<int:pk>/', album_delete, name='album delete page'),
    path('profile/details/', profile_page, name='profile page'),
    path('profile/delete/', profile_delete, name='profile delete page'),
    path('profile/create/', create_profile, name='profile create page'),
)
