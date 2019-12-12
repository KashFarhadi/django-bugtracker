from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Ticket(models.Model):
    NEW = 'New'
    IN_PROGRESS = 'In Progress'
    DONE = 'Done'
    INVALID = 'Invalid'
    STATUS_CHOICES = [
        (NEW, 'New'),
        (IN_PROGRESS, 'In_Progress'),
        (DONE, 'Done'),
        (INVALID, 'Invalid')
    ]
    title = models.CharField(max_length=300)
    date_created= models.DateTimeField(default=timezone.now)
    description = models.TextField()
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default=NEW
    )
    submitted_by = models.ForeignKey(
        User, 
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='submitted_by',
    )
    assigned_to = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='assigned_to'
    )
    completed_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='completed_by'
    )

    def __str__(self):
        return f"{self.title} - {self.status}"