from django.shortcuts import render
from models import ResumeFile
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.core.files import File

def download_forms(request,id):
	try:
		option = ResumeFile.objects.get(id=id)
	except:
		option = None

	try:
		if option:
			import urllib
			f = open(option.path, 'r')
			myfile = File(f)
			response = HttpResponse(myfile, content_type='application/pdf')
			response['Content-Disposition'] = 'attachment; filename=bio.pdf'
			return response
	except:
		messages.error(request,"There are no forms to download at this time. Call backoffice to get forms. ")
		return HttpResponseRedirect(reverse('home'))