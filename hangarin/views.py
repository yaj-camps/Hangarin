from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, TemplateView
from django.urls import reverse_lazy
from .models import Task, SubTask, Note, Category, Priority
from .forms import TaskForm, SubTaskForm, NoteForm, CategoryForm, PriorityForm


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['total_tasks']      = Task.objects.count()
        ctx['pending_tasks']    = Task.objects.filter(status='Pending').count()
        ctx['inprogress_tasks'] = Task.objects.filter(status='In Progress').count()
        ctx['completed_tasks']  = Task.objects.filter(status='Completed').count()
        ctx['recent_tasks']     = Task.objects.select_related('priority', 'category').order_by('-created_at')[:10]
        return ctx


class TaskList(ListView):
    model = Task
    context_object_name = 'object_list'
    template_name = 'task_list.html'
    paginate_by = 5

    def get_queryset(self):
        qs = Task.objects.select_related('priority', 'category').order_by('-created_at')
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(title__icontains=q)
        return qs


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'task_detail.html'


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_del.html'
    success_url = reverse_lazy('task-list')


class SubTaskCreateView(CreateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtask_form.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['task'] = get_object_or_404(Task, pk=self.kwargs['task_pk'])
        return ctx

    def form_valid(self, form):
        form.instance.parent_task = get_object_or_404(Task, pk=self.kwargs['task_pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('task-detail', kwargs={'pk': self.kwargs['task_pk']})


class SubTaskUpdateView(UpdateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtask_form.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['task'] = self.object.parent_task
        return ctx

    def get_success_url(self):
        return reverse_lazy('task-detail', kwargs={'pk': self.object.parent_task.pk})


class SubTaskDeleteView(DeleteView):
    model = SubTask
    template_name = 'subtask_del.html'

    def get_success_url(self):
        return reverse_lazy('task-detail', kwargs={'pk': self.object.parent_task.pk})


class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['task'] = get_object_or_404(Task, pk=self.kwargs['task_pk'])
        return ctx

    def form_valid(self, form):
        form.instance.task = get_object_or_404(Task, pk=self.kwargs['task_pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('task-detail', kwargs={'pk': self.kwargs['task_pk']})


class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note_del.html'

    def get_success_url(self):
        return reverse_lazy('task-detail', kwargs={'pk': self.object.task.pk})


class CategoryList(ListView):
    model = Category
    context_object_name = 'object_list'
    template_name = 'category_list.html'
    paginate_by = 10


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_del.html'
    success_url = reverse_lazy('category-list')


class PriorityList(ListView):
    model = Priority
    context_object_name = 'object_list'
    template_name = 'priority_list.html'
    paginate_by = 10


class PriorityCreateView(CreateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')


class PriorityUpdateView(UpdateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')


class PriorityDeleteView(DeleteView):
    model = Priority
    template_name = 'priority_del.html'
    success_url = reverse_lazy('priority-list')
