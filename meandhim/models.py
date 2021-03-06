from __future__ import unicode_literals

from django.db import models

# Create your models here.
class user(models.Model):
	name = models.CharField(max_length=20)
	def __str__(self):
		return self.name

class question(models.Model):
	quest = models.CharField(max_length=200)
	choice1 = models.CharField(max_length=200)
	choice2 = models.CharField(max_length=200)
	choice3 = models.CharField(max_length=200)
	choice4 = models.CharField(max_length=200, blank=True)
	choice5 = models.CharField(max_length=200, blank=True)
	def __str__(self):
		return self.quest

class response(models.Model):
	user = models.ForeignKey(user, on_delete=models.CASCADE)
	question = models.ForeignKey(question, on_delete=models.CASCADE)
	choice = models.CharField(max_length=10)
	def __str__(self):
		return self.choice

class anwser(models.Model):
	user = models.ForeignKey(user, on_delete=models.CASCADE)
	question = models.ForeignKey(question, on_delete=models.CASCADE)
	choice = models.CharField(max_length=10)
	score = models.IntegerField()
	def __str__(self):
		return self.choice
