from django.contrib import admin
from models import Project

class ProjectAdmin(admin.ModelAdmin): 
	list_display = ['__unicode__','title','precedence','active','href']
	list_editable = ['title','precedence','active','href']
	ordering = ['precedence']
	class Meta:
		model = Project

admin.site.register(Project,ProjectAdmin)


