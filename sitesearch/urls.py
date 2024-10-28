from django.urls import path, include
from django.contrib import admin
# from sitesearch.views import SiteSearchView
# from django.views.generic import TemplateView

from . import views


app_name = "sitesearch"
urlpatterns = [

    # ex: /polls/
    path("", views.index, name="index"),
    path("getter/", views.getter, name="getter"),    
    path("formtest/", views.formtest, name="formtest"),
    # path("search", views.search, name="search"),  
    
    
    # path("sitesearch/", SiteSearchView.as_view()),
    # path("about/", SiteSearchView.as_view(template_name="about.html")),    
    
    # path("", views.sexysearch_index, name="sexysearch_index"),  
    # path("sexysearch", views.sexysearch, name="sexysearch"),        

    # # ex: /polls/5/
    # path("<int:organization_id>/", views.detail, name="detail"),
    # path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # path("<int:organization_id>/entry/", views.entry, name="entry"),

]