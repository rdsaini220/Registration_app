from django.db import models

# Create your models here.
class Notice(models.Model):
    subject = models.CharField(max_length=300)
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return  self.subject