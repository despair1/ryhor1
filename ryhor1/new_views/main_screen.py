'''
Created on Nov 2, 2014

@author: despair1
'''
from django.shortcuts import render
from moves.models import entity
def main_screen(request):
    player=entity.objects.get(name="player")
    print player.location.locs.all()[0].name
    return render(request,"moves/main.html", { 'error_message': 123,
                                              'player' : player})