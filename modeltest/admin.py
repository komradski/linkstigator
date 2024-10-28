
from django.contrib import admin

from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

from .models import Organization, Link, Language, OrganizationLanguage
# Register your models here.

# admin.site.register(OrganizationLanguage)
# admin.site.register(Language)

@admin.register(OrganizationLanguage)
class OrganizationLanguageAdmin(admin.ModelAdmin):
    list_display = ("organization", "language")
    
@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("language", "iso")

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "alignment", "country", "link_count", "view_org_links")
    list_filter = ("name", "type", "alignment")  
    search_fields = ("name__contains", )  
            
    class Meta:
        ordering = ("name")    
        
    def link_count(self, obj):
        from django.db.models import Count
        result = Link.objects.filter(organization=obj).aggregate(Count("id"))
        return result["id__count"]  

    def view_org_links(self, obj):
        count = obj.link_set.count()
        url = (
            reverse("admin:modeltest_link_changelist")
            + "?"
            + urlencode({"organizations__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Link(s)</a>', url, count)

    view_org_links.short_description = "Org Links"    
             
    pass

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("type", "url", "organization")
    list_filter = ("organization", "type")
    search_fields = ("url__contains", ) 

    class Meta:
        ordering = ("organization", "type")    
    
    pass