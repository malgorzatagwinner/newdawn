from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()  # Store plain text or JSON data
    editors = models.ManyToManyField(User, related_name='editable_documents')

    def __str__(self):
        return self.title
