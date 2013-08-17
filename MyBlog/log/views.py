from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from blog.models import Post
from django import forms
from datetime import datetime
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def login(request):
	username = password = ''
        error = False
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')

                #we will use django's built in user auth system
                user = authenticate(username = username, password = password)
                if user is not None:
                    auth_login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    error = True
        return render_to_response('templates/login.html', {'error': error}, 
                                          context_instance=RequestContext(request))

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')
