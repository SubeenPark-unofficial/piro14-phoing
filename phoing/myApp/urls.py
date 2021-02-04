from django.urls import path
from . import views

app_name = 'myApp'

urlpatterns = [
    path('', view=views.main_list, name='main_list'),
    path('profile/<int:pk>/', view=views.profile_detail, name='profile_detail'),
    path('profile/<int:pk>/delete',
         view=views.profile_delete, name='profile_delete'),
    path('profile/<int:pk>/portfolio',
         view=views.profile_portfolio, name='profile_portfolio'),
    path('profile/<int:pk>/update/',
         view=views.profile_update, name='profile_update'),
    path('profile/create/', view=views.profile_create, name='profile_create'),

]