from django.db import models

class LandDivision(models.Model):
    code = models.CharField(max_length=3)
    description = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.description}"

    class Meta:
        verbose_name = "Land Division"
        verbose_name_plural = "Land Divisions"