#post_urls.py
from django.urls import path
from .views import *


urlpatterns = [
    path("",index,name="post-home"), # views altındaki index metoduna yönlendirdik.
    path("add/",add,name="post-add"),
    path("remove/",remove,name="post-remove"),
    path("edit/",edit,name="post-edit"),
    path(f"details/<int:oid>/",details)
    # path('details/<id>"',details)
]

