from django.db import models
from django.conf import settings

# Create your models here.

class Profile(models.Model):
	BG_CHOICES = (
		('blue', 'Blue'),
		('green', 'Green'),
		('yellow', 'Yellow'),
	)
	# name, slug, bg_color
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)
	bg_color = models.CharField(max_length=50, choices=BG_CHOICES)


	def __str__(self):
		return self.name

class Style(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class LinkGroup(models.Model):
    name = models.CharField(max_length=50)
    group_creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.CASCADE, default=1)
    unique_string = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return self.name
    
class Organization(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    url_suffix = models.CharField(max_length=50, null=True, blank=True)
    group = models.ForeignKey(LinkGroup, on_delete=models.CASCADE)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    
    

class Link(models.Model):
    LINKTYPE= (
        ('website', 'Website'),
        ('rss', 'RSS'),
        ('youtube', 'Youtube'),
        ('rumble', 'Rumble'),
        ('odysee', 'Odysee'),
    )    
    link_type = models.CharField(max_length=50, choices=LINKTYPE)
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    url_suffix = models.CharField(max_length=50, null=True, blank=True)
    group = models.ForeignKey(LinkGroup, on_delete=models.CASCADE)
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