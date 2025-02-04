from django.conf import settings
from django.db import models
from django.urls import reverse


class List(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

    def get_absolute_url(self):
        return reverse("view_list", args=[self.id])

    def __str__(self):
        return self.name

class Item(models.Model):
    text = models.TextField()
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)

    class Meta:
        ordering = ("id",)
        unique_together = ("list", "text")

    def __str__(self):
        return self.text
