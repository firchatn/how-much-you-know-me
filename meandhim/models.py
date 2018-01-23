from __future__ import unicode_literals

from django.db import models

# Create your models here.
class user(models.Model):
	name = models.CharField(max_length=20)
	def __str__(self):
		return self.name
"""

class choice(models.Model):
	name = models.CharField(max_length=20)
	def __str__(self):
		return self.name

class question(models.Model):
	id = models.IntegerField()
    choice = models.ForeignKey(choice, on_delete=models.CASCADE)
	def __str__(self):
		return self.name

class response(models.Model):
	user = models.ForeignKey(user, on_delete=models.CASCADE)
	question = models.ForeignKey(question, on_delete=models.CASCADE)
	def __str__(self):
		return self.user

class anwser(models.Model):
	user = models.ForeignKey(user, on_delete=models.CASCADE)
	response = models.ForeignKey(response, on_delete=models.CASCADE)
	score = models.IntegerField()
	def __str__(self):
		return self.user

"""
