from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ScrumyUser, ScrumyGoals, GoalStatus
from .forms import addUserForm, addTaskForm, changeTaskStatusForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password

# Create your views here.
def index(request):
	users = ScrumyUser.objects.all()

	return render(request, 'olufekoscrumy/index.html', {'users':users})

def add_user(request):
	
	if(request.method == "POST"):
		form = addUserForm(request.POST)
		if form.is_valid():
			
			user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
		
			user.password = make_password(password)
			user.save()
			return HttpResponseRedirect('/')
		else:
			form = addUserForm()
	else:
		form = addUserForm()


	return render(request, 'olufekoscrumy/add_user.html', {'form': form})

def get_users(request):
	users = ScrumyUser.objects.all()
	return render(request, 'olufekoscrumy/get_user.html', {'users': users})

def add_task(request):
	if request.user.is_authenticated:
		user = request.user.id
		if(request.method == "POST"):
			form = addTaskForm(request.POST)
			if(int(user) == int(request.POST.get('user'))):
				if form.is_valid():
					form.save()
					return HttpResponseRedirect('/')
				else:
					form = addTaskForm()
			else:
				return HttpResponse('you cannot add task for another user!')
		else:
			form = addTaskForm()
	else:
		return HttpResponse('you cannot access this page!, create an account to do so.')

	return render(request, 'olufekoscrumy/add_task.html', {'form': form})

def change_status(request, id):

	if request.user.is_authenticated:
		user = request.user
		user_group = user.groups.all()

		if user_group:
			if(request.method == "POST"):
				form = changeTaskStatusForm(request.POST)
				if form.is_valid():
					newstatus = request.POST.get('status')
					try:
						scrumy_goal = ScrumyGoals.objects.get(id=id)
						if scrumy_goal:
							if str(user_group[0]) == 'Owner':
								scrumy_goal.status = newstatus
								scrumy_goal.save()
								newform = form.save(commit=False)
								newform.goal_id = id
								newform.save
								return HttpResponseRedirect('/')
							elif str(user_group[0]) == 'Admin':
								if int(newstatus) == 1 or int(newstatus) == 3:
									scrumy_goal.status = newstatus
									scrumy_goal.save()
									newform = form.save(commit=False)
									newform.goal_id = id
									newform.save
									return HttpResponseRedirect('/')
								else:
									return HttpResponse('You cannot do that!')
							elif str(user_group[0]) == 'Quality Analyst':
								if int(newstatus) in [1,3,4]:
									scrumy_goal.status = newstatus
									scrumy_goal.save()
									newform = form.save(commit=False)
									newform.goal_id = id
									newform.save
									return HttpResponseRedirect('/')
								else:
									return HttpResponse('You cannot do that!')
							elif str(user_group[0]) == 'Developer':

								if int(newstatus) == 2 or int(newstatus) == 1:
									scrumy_goal.status = newstatus
									scrumy_goal.save()
									newform = form.save(commit=False)
									newform.goal_id = id
									newform.save
									return HttpResponseRedirect('/')
								else:
									return HttpResponse('You cannot do that!')
						else:
							return HttpResponse('Goal not found!')
					except ScrumyGoals.DoesNotExist:
						raise Http404('There is no goal with that id!' + str(id))

			else:
				form = changeTaskStatusForm()
		else:
			return HttpResponse('user does not belong  to any group')
	else:
		return HttpResponse('you cannot access this page!')

	return render(request, 'olufekoscrumy/change_status.html', {'form': form, 'id':id})

