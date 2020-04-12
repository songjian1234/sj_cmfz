from django.db import models

# Create your models here.


class Pic(models.Model):
    img = models.ImageField(upload_to='img')

    class Meta:
        db_table = 't_pic'