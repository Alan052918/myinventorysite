import datetime

from time import timezone
from django.db import models

# Create your models here.
class Good(models.Model):
    sku_text = models.CharField(max_length=100)
    description_text = models.CharField(max_length=200)
    previous_stop = models.CharField(max_length=50, default="")
    arrive_date = models.DateTimeField("arrival date")
    update_description_text = models.CharField(max_length=200, default="")
    update_date = models.DateTimeField("last update date")
    next_stop = models.CharField(max_length=50, default="")
    depart_date = models.DateTimeField("departure date")

    def __str__(self):
        return f"SKU: {self.sku_text}\n \
                 Description: {self.description_text}\n \
                 Arrival on: {self.arrive_date}\n \
                 Last update on: {self.update_date}\n \
                 Departure on: {self.depart_date}\n"

    def was_updated_recently(self):
        return self.update_date >= timezone.now() - datetime.timedelta(days=1)
