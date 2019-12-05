from django.db import models

# Create your models here.


class Destinations(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField(default='NA')
    img = models.ImageField(upload_to='pics')
    offer = models.BooleanField(default=False)

    # def __init__(self, name, desc, price, img, offer):
    #     self.name = name
    #     self.desc = desc
    #     self.price = price
    #     self.img = img
    #     self.offer = offer

