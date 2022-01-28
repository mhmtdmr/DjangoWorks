from datetime import datetime
from distutils.command.upload import upload
from tkinter import Image
from unittest.mock import DEFAULT
from django.db import models
from django.forms import ImageField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    ID = models.AutoField(primary_key=True)
    FullName = models.CharField(max_length=60)
    ProfileImage = models.ImageField(upload_to=f"Images/Authors/%Y/%m/%d/")
    ProfileImage_thumbnail_220_400 = ImageSpecField(source='ProfileImage',
                                     processors=[ResizeToFill(220,400)],
                                     format='JPEG',
                                     options={'quality':85})
    def __str__(self) -> str:
        return self.FullName

class Category(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)

class Tag(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=40)


class Post(models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=120,null=False)
    Body = models.TextField(null=False)
    IsPublished = models.BooleanField(default=True)
    CreateDate = models.DateTimeField(default=datetime.now())
    PublishDate = models.DateTimeField(null=True,default=datetime.now())
    Author = models.ForeignKey(Author,on_delete=models.SET('DELETED'))
    PostCategory = models.ForeignKey(Category,on_delete=models.SET("DELETED"),default="1")
    Tags = models.ManyToManyField(Tag)

    BlogImage = models.ImageField(upload_to=f"Images/Posts/%Y/%m/%d/")
    # BlogImage.name
    BlogImage_thumbnail_220_160 = ImageSpecField(source='BlogImage',
                                     processors=[ResizeToFill(220,160)],
                                     format='JPEG',
                                     options={'quality':60})

    BlogImage_thumbnail_800_320 = ImageSpecField(source='BlogImage',
                                     processors=[ResizeToFill(800,320)],
                                     format='JPEG',
                                     options={'quality':100})
    def __str__(self) -> str:
        return str(self.ID) + " " +self.Title

