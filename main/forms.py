from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
        
class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        exclude = (
            'last_login', 
            'is_staff', 
            'is_active', 
            'is_superuser', 
            'user_permissions',
            'groups',
            'username',
            'password',
            'email',
            )