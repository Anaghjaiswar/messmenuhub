from django.db import models
from django.contrib.auth.models import User

class OwnerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to the User model
    mess_name = models.CharField(max_length=255)
    # Additional fields can be added here if needed
    
    def __str__(self):
        return self.mess_name
