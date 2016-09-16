# python 
import json

# djagno
from rest_framework.views import APIView
from django.http import Http404

# app
from projects.models import Project
from serializers import ProjectSerializer

# rest
from rest_framework.response import Response
from rest_framework import status


class ProjectView(APIView):
	def get_projects(self):
		try: 
			projects = Project.objects.filter(active=True).order_by('precedence')
		except:
			projects = {} 
		return projects

	def get(self,request,format=None):
		projects = self.get_projects()
		serializer_class = ProjectSerializer
		serializer = ProjectSerializer(projects,many=True)
		return Response(serializer.data,status=200)

