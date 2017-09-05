from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import UserAccount


class RegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email')


class AccountForm(ModelForm):
    class Meta:
        model = UserAccount
        fields = '__all__'


class FindForm(ModelForm):
    class Meta:
        model = UserAccount
        fields = [
            'age',
            'sex',
        ]