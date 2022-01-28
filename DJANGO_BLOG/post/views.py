from msilib.schema import Media
from django.http import HttpResponse
from django.shortcuts import render
from .forms import AuthorForm,PostForm
from .models import *

# Create your views here.

def index(request):
    my_blogs=Post.objects.all()
    my_context = {"blogs":my_blogs}
    return render(request,"index.html",context=my_context)


def add(request):
    af = AuthorForm(request.POST or None)
    pf = PostForm(request.POST or None)
    my_context = {"authorForm":af,"postForm":pf}

    if(request.method == 'POST'):
        # authorForm = AuthorForm(request.POST)
        # if (authorForm.is_valid()):
        #     authorForm.save()
        
        postForm = PostForm(request.POST)
        if (postForm.is_valid()):
            postForm.save()
            print(postForm.BlogImage)
        
    return render(request,"add.html",context=my_context)


def remove(request):
    return HttpResponse('Hello from post remove')

def edit(request):
    return HttpResponse('Hello from post edit')

def base(request):
    return render(request,'base.html')

def details(request,oid):
    postObject = Post.objects.get(pk=oid)
    print(oid)
    return render(request,"details.html",{"v":postObject})

    # TODO: Auth.
    # TODO: Edit.
    # TODO: Delete Modal Bootstrap
