from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    name = models.CharField()
    slug = models.SlugField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(default='pic-placeholder.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def snippet(self):
        return self.description[:50] + " ..."