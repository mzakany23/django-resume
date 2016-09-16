from django.contrib import admin
from models import Blog

class BlogAdmin(admin.ModelAdmin): 
	class Meta:
		model = Blog

admin.site.register(Blog,BlogAdmin)

