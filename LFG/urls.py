from django.contrib import admin
from django.urls import path, include

from django_registration.backends.one_step.views import RegistrationView

from users.forms import CustomUserForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/register/', RegistrationView.as_view(form_class=CustomUserForm, success_url='/'),
         name='django_registration_register'),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/v1/', include('main.api.urls')),
]
