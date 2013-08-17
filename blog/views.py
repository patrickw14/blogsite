from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from blog.models import Post
from django import forms
from datetime import datetime
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

def home(request):
    blog_post_list = Post.objects.all().order_by('pub_date').reverse()[:5]

    size = Post.objects.all().count()
    if (size > 5):
        is_next_page = True
    else:
        is_next_page = False

    context = {'blog_post_list': blog_post_list, 
               'current_page_number': 1,
               'next_page_number': 2,
               'is_prev_page': False,
               'is_next_page': is_next_page}

    return render(request, 'templates/viewblogposts.html', context)

def about(request):
    return render(request, 'templates/about.html')

def contact(request):
    return render(request, 'templates/contact.html')


def viewBlogPosts(request, page_number):
    current_page_number = (int)(page_number)

    if (current_page_number < 1):
        return HttpResponseRedirect('/page/1')
        
    next_page_number = current_page_number + 1
    prev_page_number = current_page_number - 1
    y = (int)(current_page_number) * 5
    x = y - 5
    blog_post_list = Post.objects.all().order_by('pub_date').reverse()[x:y]

    if (current_page_number == 1):
        is_prev_page = False
    else:
        is_prev_page = True
    
    size = Post.objects.all().count()

    maximumPage = size / 5
    if (size % 5) != 0:
        maximumPage = maximumPage + 1

    if (current_page_number > maximumPage):
        return HttpResponseRedirect('/page/'+str(maximumPage))

    if (size > (current_page_number * 5)):
        is_next_page = True
    else:
        is_next_page = False

    context = {'blog_post_list': blog_post_list, 
               'is_next_page': is_next_page,
               'is_prev_page': is_prev_page,
               'current_page_number': current_page_number, 
               'next_page_number': next_page_number, 
               'prev_page_number': prev_page_number}

    return render(request, 'templates/viewblogposts.html', context)

@login_required
def writeNewPost(request):
    if not request.POST:
        return render_to_response('templates/writeNewPost.html', context_instance=RequestContext(request))
    response_dict = {}
    post = request.POST.get('post', False)
    author = request.POST.get('author', False)
    datePosted = datetime.now()
    dateEdited = datePosted
    title = request.POST.get('title', False)

    response_dict.update({'post': post, 'author': author, 'title': title})
    #check for errors and bad input here...
    if post and author and title:
        newPost = Post(blogPost = post, pub_date = datePosted, author = author, 
                       title = title, wasEdited = False, dateEdited = dateEdited)
        newPost.save()
        return HttpResponseRedirect('/')
    
    #if there were any errors,, then...
    else:
        if not post:
            response_dict.update({'isErrorPost': True})
        if not author:
            response_dict.update({'isErrorAuthor': True})
        if not title:
            response_dict.update({'isErrorTitle': True})

    return render_to_response('templates/writeNewPost.html', response_dict, 
                              context_instance=RequestContext(request))

def viewpost(request, blog_id):
    post = Post.objects.get(pk=blog_id)
    return render_to_response('templates/viewpost.html', {'post': post})

@login_required
def editpost(request, blog_id):
    if not request.POST:
        blogPost = Post.objects.get(pk=blog_id)
        return render_to_response('templates/editpost.html', {'blogPost': blogPost}, 
                                  context_instance=RequestContext(request))
    response_dict = {}
    post = request.POST.get('post', True)
    author = request.POST.get('author', False)
    title = request.POST.get('title', False)
    dateEdited = datetime.now()

    response_dict.update({'post': post, 'author': author, 'title': title})
    #check for errors and bad input here...
    if post and author and title:
        #save the input here
        blogPost = Post.objects.get(pk=blog_id)
        blogPost = Post(pk = blog_id, blogPost = post, pub_date = blogPost.pub_date, 
                        author = author, title = title, wasEdited = True, dateEdited = dateEdited )
        blogPost.save()
        return HttpResponseRedirect('/')    

    #if there were any errors,, then...
    else:
        if not post:
            response_dict.update({'isErrorPost': True})
        if not author:
            response_dict.update({'isErrorAuthor': True})
        if not title:
            response_dict.update({'isErrorTitle': True})

    return render_to_response('templates/editpost.html', response_dict, 
                              context_instance=RequestContext(request))
        
