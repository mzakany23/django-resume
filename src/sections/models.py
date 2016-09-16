from __future__ import unicode_literals
from ckeditor.fields import RichTextField
from django.db import models

class Section(models.Model):
	title = models.CharField(max_length=40)
	body = RichTextField(null=True,blank=True)
	precedence = models.IntegerField(default=0)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.title or 'Section %s' % self.id