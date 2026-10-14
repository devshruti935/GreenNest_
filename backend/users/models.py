from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Extended user profile with additional personal details."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=20, blank=True)
    # Additional fields can be added as needed (e.g., avatar, preferences)

    def __str__(self):
        return f"Profile of {self.user.username}"


class Address(models.Model):
    """Shipping or billing address linked to a user."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.line1}, {self.city}, {self.country}"
