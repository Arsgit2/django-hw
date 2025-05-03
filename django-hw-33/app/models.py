from django.db import models
from localflavor.us.models import USZipCodeField, USStateField

class Profile(models.Model):
    name = models.CharField(max_length=100)
    zip_code = USZipCodeField()
    state = USStateField()
    favorite_colors = models.JSONField(default=list)
    age = models.PositiveIntegerField()
