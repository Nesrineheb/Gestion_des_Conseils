# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from .views import my_view

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('expert', views.TousLesExpert, name='Expert'),
    path('these_decision', views.TousLesTheses, name='Sujet'),    

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
     
    
]
