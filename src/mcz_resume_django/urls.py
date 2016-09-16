from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

# api
from api.home.views import SkillView,AllSkillsView
from api.projects.views import ProjectView

admin.site.site_header = 'MCZ Resume Site'

(r'^ckeditor/', include('ckeditor_uploader.urls')),

# admin
urlpatterns = patterns('', 
  url(r'^$','home.views.home',name='home'),
  url(r'^admin/', include(admin.site.urls)),
  url(r'^resume-pdf/','home.views.resume_pdf_version',name='resume_pdf_version')
)

# api
urlpatterns += patterns('api.fundraiser.views',
	url(r'^api/skill/(?P<id>\d+)',SkillView.as_view(),name='api_skill'),
	url(r'^api/skills/$',AllSkillsView.as_view(),name='api_all_skills'),
	url(r'^api/projects/$',ProjectView.as_view(),name='api_all_projects'),
)

# info
urlpatterns += patterns('info.views',
	url(r'^bio/(?P<id>\d+)/$','download_forms',name='download_forms')
)

# media
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
)