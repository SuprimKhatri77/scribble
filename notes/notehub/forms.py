from django import forms
from .models import *


class CreateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title','categories','content','image']


class EditForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title','categories','content','image']


class DeleteForm(forms.Form):
    confirm = forms.BooleanField(required=True)
    label='I understand this action cannot be undone'