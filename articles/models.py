# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.png', blank=True)
	author = models.ForeignKey(User, default=None)

	"""commands to make migrations everytime we make a model
	python manage.py makemigrations
	python manage.py migrate
	"""

	def __str__(self):
		return self.title

	def snippet(self):
		#this is a model method
		if len(self.body) > 50:
			return self.body[:50] + "..."
		else:
			return self.body		
		#showing just the first 50 chars
		