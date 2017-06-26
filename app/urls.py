from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.TodoListView.as_view(), name='todos'),
	url(r'^todo/new', views.CreateTodoView.as_view(), name='todo_new'),
	url(r'^todo/(?P<pk>\d+)/$', views.TodoDetailView.as_view(), name='todo_detail'),
	url(r'^todo/(?P<pk>\d+)/edit/$', views.TodoUpdateView.as_view(), name='todo_edit'),
	url(r'^todo/(?P<pk>\d+)/done/$', views.todo_done, name='todo_done'),
	url(r'^todo/(?P<pk>\d+)/activate/$', views.todo_activate, name='todo_activate'),
	url(r'^todo/(?P<pk>\d+)/delete/$', views.TodoDeleteView.as_view(), name='todo_delete'),
]
