'''
Created on Nov 3, 2014

@author: despair1
'''
from django.shortcuts import redirect
def setup_user(request):
    if "user" not in request.session:
        print "adding user "
        request.session["user"]="player"
    return redirect("df:main")
