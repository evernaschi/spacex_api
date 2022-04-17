from unicodedata import category
from django.db import models

TYPE_CHOICES = [
    ()
]

# Create your models here.
class Task(models.Model):
    class Type(models.TextChoices):
        ISSUE = 'issue'
        BUG = 'bug'
        TASK = 'task'

    class Category(models.TextChoices):
        # The value is the LabelId in the Trello API
        MAINTENANCE = '625b2a1865db111253c2706d'
        RESEARCH = '625b2a260e06ad7c2e514278'
        TEST = '625b2a2eca30bb145948d4c7'
        BUG = '625b961941921a01845f7f8e'

    type = models.CharField(choices=Type.choices, max_length=100)
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    category = models.CharField(choices=Category.choices, max_length=100, blank=True)
