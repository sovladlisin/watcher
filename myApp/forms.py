from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from shoppls import settings
from myApp.models import Patient, UserProfileInfo
from django.utils.translation import gettext_lazy as _


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')

    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        labels = {
            'username': _('Логин'),
            'email': _('Почта'),
        }

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('name', 'surname')
        labels = {
            'name': _('Имя'),
            'surname': _('Фамилия'),
        }


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        widgets = {
            'age': forms.DateInput(attrs={'class': 'datepicker'}),
        }
        fields = ['name', 'surname', 'patronymic', 'age','room', 'cause', 'gender', 'wing']
        labels = {
            'name': _('Имя'),
            'surname': _('Фамилия'),
            'patronymic': _('Отчество'),
            'room': _('Номер палаты'),
            'age': _('Дата рождения'),
            'cause': _('Анамез'),
            'gender': _('Пол'),
            'wing': _('Отделение'),
        }

