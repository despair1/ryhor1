# -*- coding: utf-8 -*-
'''
Created on Nov 2, 2014

@author: despair1 
'''

from django.http import HttpResponse
from moves.models import locations 
from moves.models import entity,items
def init(request):
    locations.objects.all().delete()
    
    l1=locations(name="лес")
    l1.save()
    l2=locations(name="дорога")
    l2.save()
    l3=locations(name="поляна")
    l3.save()
    l1.locs.add(l2)
    l3.locs.add(l2) 
    entity.objects.all().delete()
    p1=entity(name="player",type="player",location=l1)
    p1.save()
    i1=items(name="осел", location=l2)
    i1.save()
    return HttpResponse("you in init ")