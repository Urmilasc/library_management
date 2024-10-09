from django.db import models
from django.conf import settings  # Import settings to get AUTH_USER_MODEL

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=(('available', 'Available'), ('borrowed', 'Borrowed')))
    borrowed_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name='borrowed_books')  # Reference to AUTH_USER_MODEL

    def __str__(self):
        return self.title

