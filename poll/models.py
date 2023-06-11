from django.db import models

class Question(models.Model):
    fio = models.CharField(max_length=200)
    birth_date = models.CharField(max_length=200)
    since_list = models.CharField(max_length=200)
    till_list = models.CharField(max_length=200)
    diagnos = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    telegram = models.CharField(max_length=200)
    snils = models.CharField(max_length=200, default='no')
    ip_user = models.TextField(max_length=200, default='0.0.0.0')


    def __str__(self):
        return self.fio
        return self.birth_date
        return self.since_list
        return self.till_list
        return self.diagnos
        return self.job
        return self.city
        return self.telegram

class ip_mamont(models.Model):
    ip = models.TextField(max_length=20)

    def __str__(self):
        return self.ip

    def save(self, *args, **kwargs):
        # Code to save the IP address
        super().save(*args, **kwargs)

class img(models.Model):
    image_sale = models.ImageField(blank=True)
    