from ast import mod
from django.db import models

# Create your models here.

class Prediction(models.Model):
    fullname = models.CharField(max_length=150,null=True, verbose_name='ФИО')
    age = models.IntegerField(default=1)
    gender = models.IntegerField()
    height = models.IntegerField()
    weight = models.FloatField()
    ap_hi = models.IntegerField()
    ap_lo = models.IntegerField()
    cholesterol = models.IntegerField()
    gluc = models.IntegerField()
    smoke = models.BooleanField()
    alco = models.BooleanField()
    active = models.BooleanField()
    years = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата анализа')
    cvd = models.FloatField(null=True,default=0, verbose_name='Вероятность ССЗ (%)')
    cvd_non = models.FloatField(null=True,default=0, verbose_name='Вероятность отсутствия ССЗ (%)')

    def __str__(self):
        return f"{self.fullname}"

    


