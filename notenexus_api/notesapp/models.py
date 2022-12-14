from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Node(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='userNode')
    subject_title = models.CharField(max_length=500)
    
    def __str__(self):
        return str(self.subject_title)

class Note(models.Model):
    title = models.CharField(max_length=500)
    body = models.CharField(max_length=10000)
    node = models.ForeignKey(Node, on_delete=models.CASCADE, null=False, related_name='notes')

    def __str__(self):
        return str(self.title)


