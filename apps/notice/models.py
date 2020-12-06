from django.db import models


class Notice(models.Model):
    name    = models.CharField(max_length=100)
    notice  = models.TextField(blank=True)
    status  = models.BooleanField(default=True)
    important  = models.BooleanField(default=True)
    expired_on  = models.DateField(auto_now_add=False, editable=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # change app name object to actual data name
    def __str__(self):
        return self.name
