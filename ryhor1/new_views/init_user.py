# -*- coding: utf-8 -*-
'''
Created on Nov 3, 2014

@author: despair1
'''

from django.shortcuts import redirect
from moves.models import items,entity
from moves.models import locations 
def init_user(request):
    l1=locations.objects.get(name="лес")
    #print request.POST["user"]
    p1=entity(
        name=request.POST["user"],
        type="player",location=l1)
    request.session["user"]=request.POST["user"]
    p1.save()
    """
    player=entity.objects.get(name=request.session["user"])
    item1=items.objects.get(pk=item_id)
    if player.location == item1.location:
        item1.location=None
        item1.entity=player
        item1.save()
        print "gotta"
    """
    return redirect("df:main")
