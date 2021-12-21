from django.db import models
from django.urls import reverse

class Person(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField('dob (YYYY-MM-DD)')
    address = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name 

    #to redirect detail page after updating on update page
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})

        