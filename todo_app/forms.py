from todo_app.models import Task
from django import forms
class Todoforms(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date']
