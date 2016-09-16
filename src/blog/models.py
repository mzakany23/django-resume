from __future__ import unicode_literals
from ckeditor.fields import RichTextField
from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=140)
	description = RichTextField()

	def __unicode__(self):
		return self.title
	
