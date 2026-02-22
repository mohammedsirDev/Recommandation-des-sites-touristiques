

from django.db import models

class Interest(models.Model):
    name = models.CharField(max_length=100, unique=True)  # e.g., Plage, Montagne, Culture

    def __str__(self):
        return f"{self.pk} {self.name}"
