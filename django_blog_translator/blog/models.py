from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = ((0,'Draft'),(1,'Publish'))

#this class is instantiated when an author adds a new post. 
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True) #last part of the url after the domain to access the post
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title

#to apply this to the database we have to run queries. We do that running the commands:
#       - python manage.py makemigrations
#       - python manage.py migrate 