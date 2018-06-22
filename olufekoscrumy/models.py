from django.db import models
from django.contrib.auth.models import User



# Create your models here.

ROLE_CHOICES= (
		('1', 'Owner'),
		('2', 'Admin'),
		('3', 'Quality Analyst'),
		('4', 'Developer'),
	)

class ScrumyUser(User):

	class Meta:
		proxy = True


	def __str__(self):
		return self.username

	def get_weekly_goals(self):
		return self.scrumygoals_set.filter(status=1)
		
	def get_daily_goals(self):
		return self.scrumygoals_set.filter(status=2)

	def get_verified_goals(self):
		return self.scrumygoals_set.filter(status=3)

	def get_done_goals(self):
		return self.scrumygoals_set.filter(status=4)


class ScrumyGoals(models.Model):
	user = models.ForeignKey(ScrumyUser, on_delete=models.CASCADE)
	status = models.IntegerField(null=True, default=1)
	task = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.task

	def get_task(self):
		return self.task_id



class GoalStatus(models.Model):
	GOAL_CHOICES = (
		(1, 'Weekly Task'),
		(2, 'Daily Task'),
		(3, 'Verified'),
		(4, 'Done'),
	)

	status = models.IntegerField(default=1, choices=GOAL_CHOICES)
	goal = models.ForeignKey(ScrumyGoals, on_delete=models.CASCADE)

	def __str__(self):
		return self.status
