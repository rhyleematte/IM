from django.db import models

class Schedule(models.Model):
    GROUP_CHOICES = [
        ('personal', 'Personal'),
        ('business', 'Business'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    time = models.TimeField()
    group = models.CharField(max_length=10, choices=GROUP_CHOICES, default='personal')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.get_group_display()}) on {self.date} at {self.time}"
