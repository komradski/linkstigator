        
from django.db import models
from django.conf import settings
from django.urls import reverse  # new

# from django_countries.fields import CountryField
# Create your models here.

class Person(models.Model):
    full_name = models.CharField(max_length=100)
    first = models.CharField(max_length=100)
    middle = models.CharField(max_length=100)   
    last = models.CharField(max_length=100)   
    
    # def get_absolute_url(self): # new
    #     return reverse("university_detail", args=[str(self.id)])    

class Domain(models.Model):
    name = models.CharField(max_length = 100)
    url = models.URLField(unique=True)
    json_response = models.JSONField(null=True)
    models.DateTimeField("date published")
    
    def __str__(self): # new
        return self.name    

class Article(models.Model):
    title = models.CharField(max_length=256)
    url = models.URLField(unique=True)
    json_response = models.JSONField(null=True)
    models.DateTimeField("date published")
    
        
class ArticleMeta(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    key = models.CharField(max_length = 50)
    value = models.CharField(max_length = 255)
    
class ArticleParentChild(models.Model):
    url = models.URLField(unique=True)
    response = models.JSONField(null=True)
    models.DateTimeField("date published")        
    
    
    
 