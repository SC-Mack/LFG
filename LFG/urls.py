from django.contrib import admin
from django.urls import path, include

from django_registration.backends.one_step.views import RegistrationView

from users.forms import CustomUserForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/register/', RegistrationView.as_view(success_url='/'),
         name='django_registration_register'),
    path('accounts/', include('django.contrib.auth.urls')),
]
