from django.db import models
from django.db.models.fields import CharField, TextField
from django.db.models.fields.related import ForeignKey
from django.urls import reverse


class Post(models.Model):
    title: CharField = models.CharField(max_length=200)
    author: ForeignKey = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    body: TextField = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
