from django import forms
from .models import todoitem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class create(forms.Form):
    task_name=forms.CharField(max_length=30)
    choice=(("complted","completed"),("not complete","not complted"))
    status=forms.ChoiceField(choices=choice)
    users=forms.CharField(max_length=30)

class UpdateTodoForm(forms.ModelForm):
    class Meta:
        model=todoitem
        fields='__all__'


class Registration_Form(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username"]

class Login_form(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

