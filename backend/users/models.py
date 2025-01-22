import uuid
from django.db import models
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r'^\+880\d{10}$',
    message="Phone number must be in the format '+880XXXXXXXXXX'."
)

class ParentUser(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    name = models.CharField(max_length=300)
    phone_number = models.CharField(
        max_length=14,
        validators=[phone_validator]
    )
    email = models.EmailField(unique=True, null=False, blank=False)
    address = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name

class ChildUser(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    parent = models.ForeignKey(
        ParentUser, 
        on_delete=models.CASCADE,
        related_name='children'
    )
    username = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.username