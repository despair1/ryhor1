'''
Created on Nov 2, 2014

@author: despair1
'''
from django.http import HttpResponse
from django.shortcuts import render
from moves.models import items,entity 
def inspect_item(request,item):
    item1=items.objects.get(pk=item)
    player=entity.objects.get(name=request.session["user"])
    #item1=items.objects.get(pk=item_id)
    if player.location == item1.location:
        item1.get=1
    if item1.entity == player:
        item1.drop=1
    return render(request,"moves/item.html", { 'error_message': 123,
                                              'item':item1
                                              })