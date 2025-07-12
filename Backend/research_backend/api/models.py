from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Research(models.Model):
    topic = models.CharField(max_length=200)
    research_papers = models.TextField()
    research_date = models.DateTimeField(auto_now_add=True)
    researcher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='researches')


    def __str__(self):
        return self.topic