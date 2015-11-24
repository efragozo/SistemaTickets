from django.shortcuts import get_object_or_404, render_to_response
from django.template.defaulttags import csrf_token
from django.contrib.auth import login,logout,authenticate
from django.template import RequestContext
from django.http import HttpResponseRedirect
from auten.forms import LoginForm


def login_view(request):
   mensaje = ""
   if request.user.is_authenticated():
      return HttpResponseRedirect('/')
   if request.method == 'POST':
      formulario = LoginForm(request.POST)
      if formulario.is_valid():
         username = formulario.cleaned_data['usuario']
         password = formulario.cleaned_data['password']
         usuario = authenticate(username = username, password = password)
         if usuario:
            if usuario.is_active:
               login(request, usuario)
               return HttpResponseRedirect('/')
      else:
         mensaje = "usuario y/o password incorrecto"

   form = LoginForm()
   ctx = {'form':form,'mensaje':mensaje}
   return render_to_response('login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')