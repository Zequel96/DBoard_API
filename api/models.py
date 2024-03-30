from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField(primary_key=True,max_length=100)
    price = models.IntegerField(default=0)
    banner = models.ImageField(upload_to='api/static/banners')
    generes = models.JSONField(default=list)
    platforms = models.JSONField(default=list)
