from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('add_user', views.add_user, name='add user'),
	path('get_users', views.get_users, name='get user'),
	path('add_task', views.add_task, name='add task'),
	path('change_status/<int:id>', views.change_status, name="change status"),
]
