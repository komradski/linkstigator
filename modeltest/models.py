from django.db import models
from django.conf import settings

# Create your models here.




# class Style(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name
    
# class LinkGroup(models.Model):
#     name = models.CharField(max_length=50)
#     group_creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     style = models.ForeignKey(Style, on_delete=models.CASCADE, default=1)
#     unique_string = models.CharField(max_length=8, unique=True)

#     def __str__(self):
#         return self.name    
    
    
class Organization(models.Model):
    name = models.CharField(max_length = 200)
    type: 
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.organization_name    

class LinkType(models.Model):
   

class Link(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)    
    type: 
    name = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    keyword_search_prefix = models.CharField(max_length=50, null=True, blank=True)    
    keyword_search_suffix = models.CharField(max_length=50, null=True, blank=True)
    # group = models.ForeignKey(LinkGroup, on_delete=models.CASCADE)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    
class Link(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    url_suffix = models.CharField(max_length=50, null=True, blank=True)
    group = models.ForeignKey(LinkGroup, on_delete=models.CASCADE)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title