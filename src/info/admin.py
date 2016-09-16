from django.contrib import admin
from models import Info,Resume,ResumeFile

class ResumeFileAdmin(admin.ModelAdmin): 
	class Meta:
		model = ResumeFile

admin.site.register(ResumeFile,ResumeFileAdmin)

class ResumeAdmin(admin.ModelAdmin): 
	class Meta:
		model = Resume

admin.site.register(Resume,ResumeAdmin)


class InfoAdmin(admin.ModelAdmin):
	class Meta:
		model = Info

admin.site.register(Info,InfoAdmin)

