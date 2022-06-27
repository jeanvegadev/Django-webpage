from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Usuario(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinValueValidator(5), MaxValueValidator(100)])

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old "