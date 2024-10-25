from rest_framework import serializers
from sitesearch.models import Link, LinkGroup


class LinkGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkGroup
        fields = ['id','name','group_creator','style','unique_string' ]


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id','title','url','group','creator']