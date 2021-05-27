from django.db import models


class About(models.Model):
    titile = models.CharField('title', max_length=128)
    body = models.TextField('content')

    def __str__(self):
        return self.titile