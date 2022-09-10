from django import forms
from .models import notes


class TodoForm(forms.ModelForm):
    class Meta:
        model = notes
        fields = "__all__"
