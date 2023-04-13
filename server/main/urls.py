import os
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    path('indexnew', views.indexnew, name='indexnew'),
    path('testingajax', views.testingajax, name='testingajax'),
    path('group', views.group, name='group'),
    path('ajax-datalist', views.ajax_datalist, name='ajax-datalist'),
    path('student_api', views.StudentListCreate.as_view(), name='student_api'),

]
_PATH = os.path.abspath(os.path.dirname(__file__))
urlpatterns += static('static/', document_root=os.path.join(_PATH, 'files', 'media'))
urlpatterns += staticfiles_urlpatterns()

