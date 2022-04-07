from django.db import models


class User(models.Model):

    objects = models.Manager()
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=500, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Novel(models.Model):
    objects = models.Manager()
    CATEGORY = (
        ('Romance', 'Romance'),
        ('Thriller', 'Thriller'),
        ('Fantasy', 'Fantasy'),
        ('Mystery', 'Mystery'),
    )

    title = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title