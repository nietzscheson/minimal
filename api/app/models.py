import uuid
from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique = True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
