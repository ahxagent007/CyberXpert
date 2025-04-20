from django.db import models
from ckeditor.fields import RichTextField
# pip install django-ckeditor


class Domain(models.Model):
    id = models.AutoField(primary_key=True)
    domain_no = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    body = RichTextField()

