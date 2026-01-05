from django.db import models
import uuid

# Create your models here.

class BaseMixin(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    
    class Meta:
        abstract = True