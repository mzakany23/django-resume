# django
from django.http import Http404

# rest
from rest_framework import serializers, routers, viewsets,permissions

# app
from home.models import Skill


class SkillSerializer(serializers.ModelSerializer):
	class Meta:
		model = Skill
		fields = ['name','percent','link','image']

