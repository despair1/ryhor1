'''
Created on Nov 3, 2014

@author: despair1
'''

from django.shortcuts import redirect
from moves.models import items,entity
def drop_item(request,item_id):
    player=entity.objects.get(name=request.session["user"])
    item1=items.objects.get(pk=item_id)
    if item1.entity == player:
        item1.location=player.location
        item1.entity=None
        item1.save()
        print "droped"
    
    return redirect("df:main")
