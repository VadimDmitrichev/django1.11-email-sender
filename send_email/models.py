# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Subscriber(models.Model):
	first_name = models.CharField(max_length=100, default='')
	last_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100, unique=True)

	def __str__(self):
		return self.first_name
