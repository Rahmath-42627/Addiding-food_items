from django.db import models

class Receipe(models.Model):
    receipe_name = models.CharField(max_length=100)
    text = models.TextField()
    receipe_image = models.ImageField(upload_to="recepie")
