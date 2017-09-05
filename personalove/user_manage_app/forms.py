from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import UserAccaunt


class RegForm(UserCreationForm):
    class Meta:
        model = User
fields = ('username','email')


class AccountForm(ModelForm):
    class Meta:
        model = UserAccaunt
        fields = '__all__'


class FindForm(ModelForm):
    class Meta:
        model = UserAccaunt
        fields = [
            'first_name',
            'sex',
            'birth_date'
        ]