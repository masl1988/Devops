# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns('home_application.views',
    (r'^$', 'index'),
    (r'^tasks_job/$', 'tasks_job'),
    (r'^home1/$', 'home1'),
    (r'^home2/$', 'home2'),
    (r'^dev-guide/$', 'dev_guide'),
    (r'^contactus/$', 'contactus'),
    (r'^excute/$', 'excute'),
    (r'^tasks/$', 'tasks'),
    (r'^search/$', 'search'),
    (r'^create_db', 'create_db'),
)
