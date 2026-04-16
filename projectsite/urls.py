from django.contrib import admin
from django.urls import path, include
from hangarin.views import (
    HomePageView,
    TaskList, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView,
    SubTaskCreateView, SubTaskUpdateView, SubTaskDeleteView,
    NoteCreateView, NoteDeleteView,
    CategoryList, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    PriorityList, PriorityCreateView, PriorityUpdateView, PriorityDeleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('pwa.urls')),
    path("accounts/", include("allauth.urls")),

    path('', HomePageView.as_view(), name='home'),

    path('task_list', TaskList.as_view(), name='task-list'),
    path('task_list/add', TaskCreateView.as_view(), name='task-add'),
    path('task_list/<pk>', TaskDetailView.as_view(), name='task-detail'),
    path('task_list/<pk>/edit', TaskUpdateView.as_view(), name='task-update'),
    path('task_list/<pk>/delete', TaskDeleteView.as_view(), name='task-delete'),

    path('task_list/<int:task_pk>/subtask/add', SubTaskCreateView.as_view(), name='subtask-add'),
    path('subtask/<pk>/edit', SubTaskUpdateView.as_view(), name='subtask-update'),
    path('subtask/<pk>/delete', SubTaskDeleteView.as_view(), name='subtask-delete'),

    path('task_list/<int:task_pk>/note/add', NoteCreateView.as_view(), name='note-add'),
    path('note/<pk>/delete', NoteDeleteView.as_view(), name='note-delete'),

    path('category_list', CategoryList.as_view(), name='category-list'),
    path('category_list/add', CategoryCreateView.as_view(), name='category-add'),
    path('category_list/<pk>/edit', CategoryUpdateView.as_view(), name='category-update'),
    path('category_list/<pk>/delete', CategoryDeleteView.as_view(), name='category-delete'),

    path('priority_list', PriorityList.as_view(), name='priority-list'),
    path('priority_list/add', PriorityCreateView.as_view(), name='priority-add'),
    path('priority_list/<pk>/edit', PriorityUpdateView.as_view(), name='priority-update'),
    path('priority_list/<pk>/delete', PriorityDeleteView.as_view(), name='priority-delete'),
]
