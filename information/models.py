from django.db import models
from django.contrib.auth.models import User

REPORT_STATUS = [
    ('Open', 'Open'),
    ('Resolved', 'Resolved')
]

class Report(models.Model):
    title = models.CharField(max_length=12)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=REPORT_STATUS,
        default='Open',
    )

    def __str__(self):
        return self.title

class Media(models.Model):
    report = models.ForeignKey(Report, related_name="media", on_delete=models.CASCADE)
    file = models.FileField(upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
