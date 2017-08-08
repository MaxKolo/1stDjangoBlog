# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect

from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from blog.forms import commentForm





# Create your views here.

def index(request):
    #get the blog posts that are published
    posts=Post.objects.filter(published=True)
    #return a rendered template
    return render(request, 'index.html',{'posts':posts})

def post(request,slug):
    #get the post object
    post=get_object_or_404(Post,slug=slug)
    comments=Comment.objects.filter(slug=post)
    #return the rendered template
    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            #process data here
            form_to_save = form.save(commit = False)
            
            post = get_object_or_404(Post,slug=slug)
            form_to_save.slug =  post
            form_to_save.save()
            return HttpResponseRedirect('/')
        
    else:
        form = commentForm()
    return render(request,'post.html',{'post':post, 'form':form, 'comments':comments})




