#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import url
import views

urlpatterns = [
    url('', views.PostList.as_view()),
    url('<int:pk>/', views.PostDetail.as_view()),]