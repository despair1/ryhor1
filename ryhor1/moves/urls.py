'''
Created on Nov 2, 2014

@author: despair1
'''

from django.conf.urls import patterns, url
from new_views.init_loc import init
from new_views.main_screen import main_screen
from new_views.move import move
urlpatterns=(#url(r"^$",views.index,name="index"),
             url(r"^init/",init, name="init"),
             url(r"^$",main_screen, name="main"),
             url(r"^move/(?P<loc_id>[0-9]+)/",
                 move,name="move"),
             
             )