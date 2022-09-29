from dataclasses import field
from django import forms

from todolist.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.some_flag = True
        if commit:
            instance.save()
            self.save_m2m()
        return instance

