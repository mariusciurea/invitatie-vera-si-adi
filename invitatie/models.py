from django.db import models

CONFIRMATION_CHOICES = (
   ('A', 'Abia astept'),
   ('N', 'Nu pot veni')
)


class Confirm(models.Model):
    name = models.CharField(max_length=100)
    people = models.CharField(max_length=10)
    confirm = models.CharField(choices=CONFIRMATION_CHOICES, max_length=128)

    def __str__(self):
        return f'{self.name} -> {self.people} -> {self.confirm}'

