from django.shortcuts import render
from django.conf.urls import patterns,url
from foctapp.models import Collector
from foctapp import views

urlpatterns=patterns('',url(r'^$', views.index, name='index'),
                     url(r'cjq_test', views.cjq_test, name='cjq_test'),
                     )