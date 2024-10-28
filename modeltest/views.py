import random
import string
import sys

from django.shortcuts import render
from django.db import transaction
from django.views import generic
from django.views.generic import TemplateView

from .models import Organization, Link

def index(request):
    search_links = Link.objects.all().order_by("title")
    context = {"search_links": search_links}
    return render(request, "modeltest/index.html", context)


# def get_link_object():
#     links = Link.objects.all().order_by("title")
#     # context = {"search_links": search_links}
#     return links


# for link in links():
#     print(link.url)