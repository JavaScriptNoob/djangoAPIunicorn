from django.db import models

class Drinks (models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name + "  "+self.description