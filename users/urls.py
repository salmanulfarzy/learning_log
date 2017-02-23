""" Defines URL patters for users"""

from django.conf.urls import url
from django.contrib.auth.views import login


from . import views

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    url(r'^demo/$', login, {'template_name': 'users/demo.html'}, name='demo'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),
]
