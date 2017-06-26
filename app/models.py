# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.
class Todo(models.Model):
	STATUSES = (
		('Done', 'Done'),
		('Activate', 'Activate')
	)
	task = models.CharField(max_length=256)
	created_time = models.DateTimeField(default=timezone.now)
	status = models.CharField(
				max_length=256,
				choices=STATUSES,
				default='Activate')

	def activate(self):
		self.status = 'Activate'
		self.save()

	def done(self):
		self.status = 'Done'
		self.save()

	def get_absolute_url(self):
		return reverse('todos')

	def __str__(self):
		return self.task
