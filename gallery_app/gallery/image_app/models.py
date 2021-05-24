from django.db import models

# Create your models here.


class CategoryTag(models.Model):
    category = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.category


class Picture(models.Model):
    description = models.CharField(max_length=200, null=True)
    picture = models.ImageField(null=True, blank=True, upload_to='images/')
    categories = models.ForeignKey(CategoryTag, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.description


    
    