from django.db import models

# Create your models here.

class Tree(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    CHOICES = (
    (1, 'クール'),
    (2, 'かわいい'),
    (3, 'ロマンティック'),
    )
    look = models.IntegerField(choices=CHOICES)
    data = models.TextField(max_length=5000)


    def __str__(self):
        return self.name + ", " +str(self.look)


