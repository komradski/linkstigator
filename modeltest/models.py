from django.db import models
from django.conf import settings

from django_countries.fields import CountryField
# Create your models here.

class Organization(models.Model):
    ORGTYPE= (
        ('news','News'),
        ('ngo','NGO'),
            
    )
    ORG_ALIGNMENT = (
        ('assess','TBD'),
        ('western','Western'),
        ('non-western','Non-Western'),
        ('mixed','Mixed'),
    )
    name = models.CharField(max_length = 255)
    type = models.CharField(max_length=100, choices=ORGTYPE, default='news')
    alignment = models.CharField(max_length=100, choices=ORG_ALIGNMENT, default='assess')
    country = CountryField(null=True)
    # create_dt = models.DateTimeField("date published")
    # creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    
    # edit_dt = models.DateTimeField("date edited")
    # editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ("name", "type")
    
    
    
# class Person(models.Model):
#     first = 
#     middle
#     last = 
#     name = 
#     name_last_first
#     first_middle_last
#     affiliation = PersonOrganization
        
# class PersonOrganization(models.Model):
# class PersonOrganization(models.Model):
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)    
#     organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    
#     def __str__(self):
#         return self.person.name + ' : ' + self.organization.name
    
#     class Meta:
#         unique_together = [["person", "organization"]]
        
        
class Language(models.Model):    
    iso = models.CharField(max_length = 20, unique=True)
    language = models.CharField(max_length = 50, unique=True)
    
    def __str__(self):
        return self.iso + ' : ' + self.language
    
    
class OrganizationLanguage(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.organization.name + ' : ' + self.language.language
    
    class Meta:
        unique_together = [["organization", "language"]]
    
    

class Link(models.Model):
    LINKTYPE = (
        ('mainsite','Main Website'),
        ('website','Website'),
        ('rss','RSS'),
        ('linktree','Linktree'),        
        ('fb','Facebook'),
        ('x','X'),
        ('insta','Instagram'),
        ('youtube','Youtube'),
        ('rumble','Rumble'),
        ('odysee','Odysee'),
    )    
    # LANGUAGE = (
    #     ('en','English'),
    #     ('ar','Arabic'),

    # )      
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length = 255, blank=True, default='')
    type = models.CharField(max_length=100, choices=LINKTYPE, default='mainsite')
    # language = models.CharField(max_length=100, choices=LANGUAGE, default='en')
    language = models.ForeignKey(Language,
                            models.SET_NULL,
                            blank=True,
                            null=True
                            # choices=Language
                            )
    url = models.URLField(unique=True)
    
    keyword_search_prefix = models.CharField(max_length=50, null=True, blank=True)    
    keyword_search_suffix = models.CharField(max_length=50, null=True, blank=True)
    # group = models.ForeignKey(LinkGroup, on_delete=models.CASCADE)
    # create_dt = models.DateTimeField("date published")
    # creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    
    # edit_dt = models.DateTimeField("date edited")
    # editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  

    def __str__(self):
        return self.organization.name + ': ' + self.type + ': ' + self.url
    
    class Meta:
        ordering = ("organization", "url")
    
    
# class Link(models.Model):
#     title = models.CharField(max_length=255)
#     url = models.URLField(unique=True)
#     url_suffix = models.CharField(max_length=50, null=True, blank=True)
#     group = models.ForeignKey(LinkGroup, on_delete=models.CASCADE)
#     creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title



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