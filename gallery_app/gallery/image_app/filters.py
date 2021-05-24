import django_filters

from .models import *

class PictureFilter(django_filters.FilterSet):
    class Meta:
        model = Picture
        fields = ['description', 'categories']