import os.path
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    (r'^$', 'hotaru.views.index'),
    (r'^res/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.abspath('./templates'), 'show_indexes': True}),
    (r'^(?P<template>.+)$', 'hotaru.views.show'),
)
