from django.db import models
from django.db.models import CASCADE


class User(models.Model):
    tg_id = models.BigIntegerField()
    tg_name = models.CharField(max_length=32)
    user_name = models.CharField(max_length=100)
    user_surname = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user_name} {self.user_surname}'


class Brand(models.Model):
    brand_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.brand_name}'


class Size(models.Model):
    size_us = models.IntegerField()
    size_rus = models.IntegerField()
    size_euro = models.IntegerField()
    size_uk = models.IntegerField()
    size_centimeters = models.IntegerField()

    def __str__(self):
        return f'{self.size_euro}'


class Sneaker(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='models')
    model_name = models.CharField(max_length=100)


class Sku(models.Model):
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    sneaker = models.ForeignKey(Sneaker, on_delete=models.CASCADE)
    color = models.CharField()
    image_url = models.CharField()
    price = models.IntegerField()
    count = models.IntegerField()


class CartItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sku = models.ForeignKey(Sku, on_delete=models.CASCADE)
    quantity = models.IntegerField()
