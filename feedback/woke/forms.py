from django import forms
from .models import db

class db_form(forms.ModelForm):
    class Meta:
        model = db
        fields = "__all__"
       