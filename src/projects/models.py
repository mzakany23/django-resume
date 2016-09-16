from __future__ import unicode_literals
from ckeditor.fields import RichTextField

from django.db import models

class Project(models.Model):
	title = models.CharField(max_length=40,null=True,blank=True)
	description = RichTextField(blank=True,null=True)
	thumbnail = models.ImageField(upload_to='projects',blank=True,null=True)
	precedence = models.IntegerField(default=0)
	active = models.BooleanField(default=True)
	href=models.CharField(max_length=100,blank=True,null=True)

	def __unicode__(self):
		return self.title
