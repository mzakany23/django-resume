# django
from django.http import Http404

# rest
from rest_framework import serializers, routers, viewsets,permissions

# app
from projects.models import Project


class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = ['title','description','thumbnail','href']

