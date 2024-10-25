import random
import string
import sys

from django.shortcuts import render
from django.db import transaction
from django.views import generic
from django.views.generic import TemplateView



def index(request):
    # search_links = Link.objects.order_by("title")
    # context = {"search_links": search_links}
    return render(request, "index.html")