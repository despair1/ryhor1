'''
Created on Nov 2, 2014

@author: despair1
'''

from django.conf.urls import patterns, url
from new_views.init_loc import init
from new_views.main_screen import main_screen
from new_views.move import move
from new_views.item import inspect_item
from new_views.item_get import get_item
from new_views.setup_user import setup_user
from new_views.item_drop import drop_item
from new_views.init_user import init_user
urlpatterns=(#url(r"^$",views.index,name="index"),
             url(r"^init/",init, name="init"),
             url(r"^init_user/",init_user, name="init_user"),
             url(r"^$",setup_user, name="setup"),
             url(r"^main/",main_screen, name="main"),
             url(r"^move/(?P<loc_id>[0-9]+)/",
                 move,name="move"),
             url(r"^item/(?P<item>[0-9]+)/",
                 inspect_item,name="item"),
             url(r"^item_get/(?P<item_id>[0-9]+)/",
                 get_item,name="item_get"),
             url(r"^item_drop/(?P<item_id>[0-9]+)/",
                 drop_item,name="item_drop"),  
             
             )