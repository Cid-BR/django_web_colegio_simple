# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from inicio import views

urlpatterns = patterns('',
		url(r'^$', views.inicio, name="inicio_redirect"),
		url(r'^inicio/$', views.inicio, name='inicio'),
		url(r'^colegio/$', views.colegio, name='colegio'),
		url(r'^docentes/$', views.docentes, name='docentes'),
		url(r'^estudiantes/$', views.estudiantes, name='estudiantes'),
		url(r'^blog/$', views.blog, name='blog'),
		url(r'^sislogin/$', views.sislogin, name='sislogin'),
	)
