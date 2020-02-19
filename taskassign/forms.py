from django import forms
from .models import tasks


class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=255, label='task')

    class Meta:
        model = tasks
        fields = ['title','description']