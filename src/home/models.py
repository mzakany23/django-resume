from django.db import models
from ckeditor.fields import RichTextField

class Skill(models.Model):
	name = models.CharField(max_length=40)
	percent = models.DecimalField(max_digits=10,decimal_places=2)
	link = models.CharField(max_length=100,blank=True,null=True)
	image = models.ImageField(upload_to='skill-images',blank=True,null=True)


	def __unicode__(self):
		return self.name

class Experience(models.Model):
	name = models.CharField(max_length=40,blank=True,null=True)
	title = RichTextField()
	dates = models.CharField(max_length=40,blank=True,null=True)
	precedence = models.IntegerField(default=0)
	description = RichTextField()

	def __unicode__(self):
		return self.dates

class Hobby(models.Model):
	title = models.CharField(max_length=140)
	
	def __unicode__(self):
		return self.title

class Education(models.Model):
	date = models.CharField(max_length=50)
	title = models.CharField(max_length=140)
	description = RichTextField()

	def __unicode__(self):
		return self.title