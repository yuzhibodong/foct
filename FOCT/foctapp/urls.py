from django.shortcuts import render
from django.conf.urls import patterns,url
from foctapp.models import Collector
from foctapp import views

urlpatterns=patterns('',url(r'^$', views.index, name='index'),
                     url(r'cjq_test', views.cjq_test, name='cjq_test'),
                     url(r'search',views.connected,name='connected'),
                     url(r'fsj',views.fsj_test,name='fsj_test'),
                     url(r'qurry',views.fsj_qurry,name='fsj_qurry'),
                     url(r'data_statistics',views.statistics,name='statistics')
                     )