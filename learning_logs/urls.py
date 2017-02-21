"""Defines URL patters for learning_logs."""

from django.conf.urls import url
from . import views

urlpatterns = [
        #  Home page
        url(r'^$', views.index, name='index'),

        # Show all topics
        url(r'^topics/$', views.topics, name='topics'),

        # Page for new topic
        url(r'^new_topic/$', views.new_topic, name='new_topic'),

        # Detail page for a single topic
        url(r'topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    ]
