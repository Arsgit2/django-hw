from django.db import models
from markup.fields import MarkupField

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = MarkupField(markup_type='bbcode')
    def __str__(self):
        return self.title
