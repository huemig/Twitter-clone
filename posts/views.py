from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PostForm
from .models import Post
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/') 
        else:
            return HttpResponseRedirect ('form.errors.as_json()')
    posts = Post.objects.all().order_by('-created_at')[:20]
    form = PostForm
    
    return render(request, 'posts.html', {'posts' : posts})
    
    
def delete(request, post_id):
    post = Post.objects.get(id= post_id) 
    post.delete()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    post = Post.objects.get(id= post_id)
    if request.method == 'POST':
        form =  PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else : 
           return HttpResponseRedirect(form.errors.as_json())
    return(
        render(request, "edit.html",{"post":post}))
    
def like(request, post_id):
    post = Post.objects.get(id= post_id)
    counter = post.like+1
    post.like = counter
    post.save()
    return HttpResponseRedirect('/')
    
    
    # output = 'POST ID is ' + str(post_id)
    #return HttpResponse(output)
