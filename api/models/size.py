from django.db import models


class Size(models.Model):
    size_rus = models.IntegerField()
    size_centimeters = models.IntegerField(default=0)

    def __str__(self):
        return f'Rus: {self.size_rus} - {self.size_centimeters} сm'

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural= 'Размеры'
