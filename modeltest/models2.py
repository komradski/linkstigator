        
from django.db import models
from django.conf import settings

from django_countries.fields import CountryField
# Create your models here.



class ArticleLink(models.Model):
    url = models.URLField(unique=True)
    response = models.JSONField(null=True)
    models.DateTimeField("date published")
    
    
class ArticleLinkMeta(models.Model):
    articlelink = models.ForeignKey(ArticleLink, on_delete=models.CASCADE)
    key = models.CharField(max_length = 50)
    value = models.CharField(max_length = 255)
    
 