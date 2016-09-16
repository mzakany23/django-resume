from django.contrib import admin
from models import Section

class SectionAdmin(admin.ModelAdmin): 
	class Meta:
		model = Section

admin.site.register(Section,SectionAdmin)

