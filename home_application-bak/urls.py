# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns('home_application.views',
    (r'^$', 'home'),
    (r'^excute_task/$', 'excute_task'),
    (r'^home1/$', 'home1'),
    (r'^home2/$', 'home2'),
    (r'^dev-guide/$', 'dev_guide'),
    (r'^contactus/$', 'contactus'),
    (r'^excute/$', 'excute'),
)
