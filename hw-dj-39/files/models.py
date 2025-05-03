
from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
