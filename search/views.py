from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from blog.models import Post
from django import forms

#right now, system only supports searches of 1 term - add multiple term support later
def search(request):
    if 'q' in request.GET:
        search_results = Post.objects.filter(author__icontains= request.GET['q'] ).order_by('pub_date').reverse()
        return render_to_response('templates/search.html', {'search_results': search_results})
    else:
        return HttpResponseRedirect('/')
