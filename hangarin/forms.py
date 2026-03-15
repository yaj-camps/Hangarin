from django.forms import ModelForm
from django import forms
from .models import Task, SubTask, Note, Category, Priority


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'status', 'priority', 'category']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class SubTaskForm(ModelForm):
    class Meta:
        model = SubTask
        exclude = ['parent_task']


class NoteForm(ModelForm):
    class Meta:
        model = Note
        exclude = ['task']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class PriorityForm(ModelForm):
    class Meta:
        model = Priority
        fields = "__all__"