from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from django.contrib.auth.forms import UserChangeForm as DjangoUserChangeForm
from .models import User


class UserCreationForm(DjangoUserCreationForm):
    class Meta:
        model = User
        fields = '__all__'


class UserChangeForm(DjangoUserChangeForm):
    class Meta:
        model = User
        fields = '__all__'
