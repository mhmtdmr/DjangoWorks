from django.contrib import admin
from post.models import *
# Register your models here.
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
