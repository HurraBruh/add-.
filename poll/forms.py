from .models import Question, ip_mamont
from django import forms
from django.forms import ModelForm

class QuestionForm(ModelForm):
	class Meta:
		model = Question
		fields = ('fio', 'birth_date', 'since_list', 'till_list', 'diagnos', 'job', 'city', 'telegram')

		widget = {
		'fio': forms.TextInput(attrs={'class': 'form-control'}),
		'birth_date': forms.TextInput(attrs={'class': 'form-control'}),
		'since_list': forms.TextInput(attrs={'class': 'form-control'}),
		'till_list': forms.TextInput(attrs={'class': 'form-control'}),
		'diagnos': forms.TextInput(attrs={'class': 'form-control'}),
		'snils': forms.TextInput(attrs={'class': 'form-control'}),
		'job': forms.TextInput(attrs={'class': 'form-control'}),
		'city': forms.TextInput(attrs={'class': 'form-control'}),
		'telegram': forms.TextInput(attrs={'class': 'form-control'}),
		}

class IP(ModelForm):
	class Meta:
		model = ip_mamont
		fields = '__all__'