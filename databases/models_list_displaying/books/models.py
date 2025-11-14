# coding=utf-8

from django.db import models


class Book(models.Model):
    name = models.CharField(u'Название', max_length=255)
    author = models.CharField(u'Автор', max_length=255)
    pub_date = models.DateField(u'Дата публикации')

    class Meta:
        ordering = ["pub_date"]  # sorted by publication date

    def __str__(self):
        return f"{self.name} {self.author}"
