from __future__ import unicode_literals

from django.db import models

# Create your models here.
class user(models.Model):
	name = models.CharField(max_length=20)
	def __str__(self):
		return self.name
"""
class response(models.Model):
	name = models.CharField(max_length=20)
	def __str__(self):
		return self.name


class answer(models.Model):
	name = models.CharField(max_length=20)
	def __str__(self):
		return self.name

class question(models.Model):
	id = models.IntegerField()
	name = models.CharField(max_length=20)
	def __str__(self):
		return self.name

class choice(models.Model):
	id = models.IntegerField()
	name = models.CharField(max_length=20)
	def __str__(self):
		return self.name
"""
