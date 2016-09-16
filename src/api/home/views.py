# python 
import json

# djagno
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import Http404

# app
from home.models import Skill
from serializers import SkillSerializer

# rest
from rest_framework.response import Response
from rest_framework import status

class UtilityMixin:
	def get_skill(self,id):
		try:
			skill = Skill.objects.get(id=id)
		except: 
			skill = None
		return skill 
	def get_skills(self):
		try:
			skills = Skill.objects.order_by('-percent')
		except:
			skills = None
		return skills

class SkillView(APIView,UtilityMixin):

	def post(self,request,id):
		record = self.get_skill(id)
		serializer_class = SkillSerializer
		serializer = SkillSerializer(record)
		return Response(serializer.data,status=200)

class AllSkillsView(APIView,UtilityMixin):

	def get(self,request,format=None):
		skills = self.get_skills()
		serializer_class = SkillSerializer
		serializer = SkillSerializer(skills,many=True)
		return Response(serializer.data,status=200)

