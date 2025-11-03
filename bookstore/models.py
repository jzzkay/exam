from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    created_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='books/images/', null=True, blank=True)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='books/files/', null=True, blank=True)
    author = models.CharField(max_length=255)
    number_of_views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title