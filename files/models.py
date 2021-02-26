from django.db import models

# Create your models here.
class Document(models.Model):
    name = models.CharField(null="False", blank = "False", max_length= 64 )
    files = models.FileField(upload_to='media')

    def __str__(self):
        return str(self.name) if self.name else ''