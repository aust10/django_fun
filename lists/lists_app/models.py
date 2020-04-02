import datetime
from django.db import models

from django.utils import timezone


class ListItem(models.Model):
    items = models.CharField(max_length=200)
    pub_date = models.DateTimeField('published date')
    comp_date = models.DateTimeField('compleated date', null= True, blank=True)
    is_comp = models.BooleanField(default=False)

    def __str__(self):
        return self.items