from django.db import models

class Monument(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    year_built = models.PositiveIntegerField()
    image = models.ImageField(upload_to='monuments/', null=True, blank=True)

    def __str__(self):
        return self.name