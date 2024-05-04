from django.db import models

class Recepie(models.Model):
    recepie_name = models.CharField(max_length=100)
    recepie_description = models.TextField()
    receipe_image = models.ImageField(upload_to="recepie")