'''
Created on Nov 2, 2014

@author: despair1
'''
from django.shortcuts import redirect
from moves.models import items,entity
def get_item(request,item_id):
    player=entity.objects.get(name=request.session["user"])
    item1=items.objects.get(pk=item_id)
    if player.location == item1.location:
        item1.location=None
        item1.entity=player
        item1.save()
        print "gotta"
    
    return redirect("df:main")