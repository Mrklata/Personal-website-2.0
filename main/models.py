from django.db import models
from django.urls import reverse


class Language(models.Model):
    title = models.CharField(max_length=100)
    desc_short = models.TextField()
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('skill', kwargs={'title': self.title})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"
