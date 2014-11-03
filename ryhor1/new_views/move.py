'''
Created on Nov 2, 2014

@author: despair1
'''
from django.http import HttpResponse
from moves.models import entity,locations
from new_views.main_screen import main_screen
from django.shortcuts import redirect
def move(request,loc_id):
    
    
    player=entity.objects.get(name=request.session["user"])
    #print loc_id
    for i in player.location.locs.all():
        if int(i.pk) == int(loc_id) :
            player.location=i
            player.save()
            #print "in if"
            break
        #print i.pk
    return redirect("df:main")
    return HttpResponse("you in move ")
    