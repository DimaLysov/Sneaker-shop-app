from django.db import models


class User(models.Model):
    # tg_id = models.BigIntegerField()
    # tg_name = models.CharField(max_length=32)
    user_name = models.CharField(max_length=100)
    user_surname = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user_name} {self.user_surname}'
