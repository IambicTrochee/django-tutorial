from django.db import models
from django.utils import timezone
# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def submit(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.subject