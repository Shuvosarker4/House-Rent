from django.db import models
from users.models import User
from advertisement.models import Advertisement

class RentRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rent_requests')
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='rent_requests')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.advertisement.title}"