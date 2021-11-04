from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('accounts/change-password/', views.change_password, name = 'change_password'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register, name='register'),
    path('accounts/<username>', views.profile, name='profile'),
    path('accounts/edit/<username>', views.edit_profile, name='edit_profile'),
    path('addToList/', views.addToList, name='addToList'),
    path('getWishedId/', views.getWishedId, name='getWishedId'),
    path('removeGame/', views.removeGame, name='removeGame'),
]
