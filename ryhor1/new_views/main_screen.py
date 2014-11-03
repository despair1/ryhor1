'''
Created on Nov 2, 2014

@author: despair1
'''
from django.shortcuts import render
from moves.models import entity,locations
def main_screen(request):
    #print request.session["user"]
    player=entity.objects.get(name=request.session["user"])
    #print player.location.locs.all()[0].name
    """
    items=player.location.items.all()
    for i in items:
        print i.name """ 
    return render(request,"moves/main.html", { 'error_message': 123,
                                              'player' : player})