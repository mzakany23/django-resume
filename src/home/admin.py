from django.contrib import admin
from models import Skill, Experience, Hobby, Education

class SkillAdmin(admin.ModelAdmin):
	list_display = ['__unicode__','name','percent','link','image']
	list_editable = ['name','percent','link']
	ordering = ['-percent']
	class Meta:
		model = Skill

admin.site.register(Skill,SkillAdmin)

class ExperienceAdmin(admin.ModelAdmin): 
	list_display = ['name','precedence']
	list_editable = ['precedence']
	class Meta:
		model = Experience

admin.site.register(Experience,ExperienceAdmin)

class HobbyAdmin(admin.ModelAdmin): 
	class Meta:
		model = Hobby

admin.site.register(Hobby,HobbyAdmin)

class EducationAdmin(admin.ModelAdmin): 
	class Meta:
		model = Education

admin.site.register(Education,EducationAdmin)
