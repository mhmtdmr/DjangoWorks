#post_urls.py
from django.urls import path
from .views import *


urlpatterns = [
    path("",index,name="post-home"), # views altındaki index metoduna yönlendirdik.
    path("add/",add,name="post-add"),
    path("remove/",remove,name="post-remove"),
    path("edit/",edit,name="post-edit"),
    path("edit/<int:pid>/",edit,name="post-edit"),
    path(f"details/<int:oid>/",details),
    path('login/',login,name="user-login")
    # path('details/<id>"',details)
]

