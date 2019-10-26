from django.db import models

# Create your models here.

class Tree(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    CHOICES = (
    (1, 'クール'),
    (2, 'かわいい'),
    (3, 'おしゃれ'),
    (4, 'ばえ'),
    (5, '読める！'),
    (6, 'おもしろい'),

    )
    look = models.IntegerField(choices=CHOICES)
    data = models.TextField(max_length=5000)
    lighted = models.BooleanField(default=False)


    def __str__(self):
        return self.name + ", " +str(self.look) + ", " +str(self.lighted)



