from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.TextField() #essa função define o schema do model
    content = models.TextField()
