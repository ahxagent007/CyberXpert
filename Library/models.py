from django.db import models
from ckeditor.fields import RichTextField
# pip install django-ckeditor


class domain(models.Model):
    id = models.IntegerField(primary_key=True)
    domain_no = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    body = models.RichTextField()

