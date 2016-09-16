from django.core.urlresolvers import reverse
from django.shortcuts import render
from models import Skill, Experience, Hobby
from sections.models import Section
from info.models import Info,ResumeFile
from projects.models import Project

def home(request):
	skills = Skill.objects.order_by('-percent')
	sections = Section.objects.filter(active=True).order_by('precedence')
	experience = Experience.objects.order_by('precedence') 
	projects = Project.objects.filter(active=True).order_by('precedence')
	hobbies = Hobby.objects.all()
	info = Info.objects.first()
	files = ResumeFile.objects.filter(active=True)

	main_context = {
		'skills' : skills,
		'sections' : sections,
		'experience' : experience,
		'hobbies' : hobbies,
		'info' : info,
		'projects' : projects,
		'files' : files
	}
	main_context['pdf'] = False
	template = 'home/base.html'
	return render(request,template,main_context)

def resume_pdf_version(request):
	skills = Skill.objects.order_by('-percent')
	sections = Section.objects.filter(active=True).order_by('precedence')
	experience = Experience.objects.order_by('precedence') 
	projects = Project.objects.filter(active=True).order_by('precedence')
	hobbies = Hobby.objects.all()
	info = Info.objects.first()
	files = ResumeFile.objects.filter(active=True)
	
	pdf_context = {
		'skills' : skills,
		'sections' : sections,
		'experience' : experience,
		'hobbies' : hobbies,
		'info' : info,
		'projects' : projects
	}
	pdf_context['pdf'] = True
	template = 'home/base.html'
	return render(request,template,pdf_context)


