from django.db import models
from ckeditor.fields import RichTextField
from mcz_resume_django.settings import MEDIA_ROOT

resume_dir = "%s/resumes" % MEDIA_ROOT

class Info(models.Model):
	last_updated = models.CharField(max_length=40,blank=True,null=True)
	main_title = RichTextField(null=True)
	sub_title = RichTextField(null=True)
	mcz_image = models.ImageField(upload_to='headshot',blank=True,null=True)
	
	def __unicode__(self):
		return self.last_updated

class Resume(models.Model):
	name = models.CharField(max_length=50)
	resume = models.FileField(upload_to='resumes/')

	def __unicode__(self):
		return self.name

class ResumeFile(models.Model):
	name = models.CharField(max_length=50)
	path = models.FilePathField(path=resume_dir,null=True,blank=True)
	active = models.BooleanField(default=False)

	def __unicode__(self):
		return self.name

	def download_url(self):
		return "/bio/%s" % self.id