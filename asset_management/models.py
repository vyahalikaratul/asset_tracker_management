# models.py

from django.db import models
from django.utils import timezone
import uuid

# Function to generate a 16-digit asset code


def generate_asset_code():
    """
    Generates a 16-digit asset code using a UUID.

    Returns:
        str: A 16-digit asset code.
    """
    return str(uuid.uuid4().int)[:16]


class AssetType(models.Model):
    """Model representing a type of asset."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Asset(models.Model):
    """Model representing an asset."""
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=16, unique=True, default=generate_asset_code, editable=False)
    # code = models.UUIDField(default=uuid.uuid4, editable=False)
    asset_type = models.ForeignKey(AssetType, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='asset_images/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class AssetImage(models.Model):
    """Model representing an image associated with an asset."""
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='asset_images/')

    def __str__(self):
        return f"Image for {self.asset.name}"
