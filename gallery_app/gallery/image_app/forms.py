from .models import Picture
from django.forms import ModelForm



class ImageForm(ModelForm):
    class Meta:
        model = Picture
        fields = ['description', 'picture', 'categories']