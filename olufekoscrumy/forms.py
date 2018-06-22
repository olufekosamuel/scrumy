from django.forms import ModelForm
from .models import ScrumyUser, ScrumyGoals, GoalStatus
from django.contrib.auth.models import User
from django import forms

class addUserForm(ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)
	class Meta:
		model = User
		fields = ['first_name', 'last_name','username','email', 'password',]


class addTaskForm(ModelForm):
	class Meta:
		model = ScrumyGoals
		fields = ['user','task']

class changeTaskStatusForm(ModelForm):
	class Meta:
		model = GoalStatus
		fields = ['status']

