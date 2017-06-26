# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView,
									DetailView,UpdateView,
									DeleteView)

from app.forms import TodoForm
from app.models import Todo

class TodoListView(ListView):
	template_name = 'todo_list.html'
	model = Todo

class CreateTodoView(CreateView):
	template_name = 'todo_create.html'
	redirect_field_name = 'todo_detail.html'
	form_class = TodoForm
	model = Todo

class TodoDetailView(DetailView):
	model = Todo
	template_name = 'todo_detail.html'

class TodoUpdateView(UpdateView):
	template_name = 'todo_create.html'
	redirect_field_name = 'todo_detail.html'
	form_class = TodoForm
	model = Todo

class TodoDeleteView(DeleteView):
	model = Todo
	template_name = 'todo_confirm_delete.html'
	success_url = reverse_lazy('todos')


def todo_activate(request, pk):
	todo = get_object_or_404(Todo, pk=pk)
	todo.activate()
	return redirect('todos')

def todo_done(request, pk):
	todo = get_object_or_404(Todo, pk=pk)
	todo.done()
	return redirect('todos')
