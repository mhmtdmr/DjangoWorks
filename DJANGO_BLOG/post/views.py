from msilib.schema import Media
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from .forms import AuthorForm,PostForm
from .models import *

from django.contrib.auth import logout,authenticate, login


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






def edit(request,pid):
    post = get_object_or_404(Post,pk=pid)
    if(request.method == "POST"):
        form = PostForm(request.POST,instance=Post)
        if(form.is_valid()):
            post = form.save(commit=False)
            return redirect('details', pk=post.pk)
    else:
        form = PostForm(instance=Post)
    return render(request,'edit.html',{'form': form})









    

def base(request):
    return render(request,'base.html')

def details(request,oid):
    postObject = Post.objects.get(pk=oid)
    print(oid)
    return render(request,"details.html",{"post":postObject})

    # TODO: Auth. https://docs.djangoproject.com/en/4.0/topics/auth/default/#user-objects
    # TODO: Edit.
    # TODO: Delete Modal Bootstrap

    # u:p => demir
from django.contrib.auth.decorators import login_required

@login_required()
def loginTest(request):
    return HttpResponse("LOGIN IS OK")

# @login_required(login_url='/accounts/login/')
# def my_view(request):
#     ...


def login(request):
    loginForm = AuthorForm(request.POST or None)
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




    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...


# If the user isn’t logged in, redirect to settings.LOGIN_URL, passing the current absolute path in the query string. Example: /accounts/login/?next=/polls/3/.


# if request.user.is_authenticated:
#     # Do something for authenticated users.
#     ...
# else:
#     # Do something for anonymous users.
#     ...


from django.contrib.auth import logout,authenticate, login

# def logout_view(request):
#     logout(request)
#     # Redirect to a success page.

# def my_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#         ...
#     else:
#         # Return an 'invalid login' error message.
#         ...


# from django.shortcuts import render

# def my_view(request):
#     if not request.user.is_authenticated:
#         return render(request, 'myapp/login_error.html')
#     # ...


# {% if user.is_authenticated %}
#      <a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
# {% endif %}