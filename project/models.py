from django.db import models
from django.urls import reverse


class Portfolio(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    short_description = models.TextField()
    photo_id = models.IntegerField(null=True, blank=True)
    url_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio-detail', args=[str(self.id)])


