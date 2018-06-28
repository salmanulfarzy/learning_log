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

        # Page for edition topic title
        url(r'^edit_topic/(?P<topic_id>\d+)$', views.edit_topic, name='edit_topic'),

        # Detail page for a single topic
        url(r'topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

        # Page for adding new entry
        url(r'new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

        # Page for editing an entry
        url(r'edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
        url(r'delete_entry/(?P<entry_id>\d+)/$', views.delete_entry, name='delete_entry')
    ]
