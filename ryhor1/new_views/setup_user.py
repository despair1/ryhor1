'''
Created on Nov 3, 2014

@author: despair1
'''
from django.shortcuts import redirect
from django.shortcuts import render
def setup_user(request):
    #return render(request,"moves/setup_user.html", { 'error_message': 123,
    #                                         })
    if "user" not in request.session:
        print "adding user "
        return render(request,"moves/setup_user.html", { 'error_message': 123,
                                              })
        request.session["user"]="player"
    return redirect("df:main")
