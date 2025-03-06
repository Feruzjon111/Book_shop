from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    number = models.PositiveIntegerField()
    genre = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', default='defaults/book.jpg' ,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Books"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title