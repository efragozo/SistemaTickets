from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response,redirect
from django.template.defaulttags import csrf_token
from django.contrib.auth import login,logout,authenticate
def index(request):
	if request.user.is_authenticated():
	    return render_to_response("index.html",{},
	    context_instance=RequestContext(request))  
	else: 
	   return redirect("/login")