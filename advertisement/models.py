from django.db import models
from users.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

class Advertisement(models.Model):
    CATEGORY_CHOICES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('villa', 'Villa'),
        ('room', 'Room'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='advertisements')
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    advertisement = models.ForeignKey(Advertisement,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ratings = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review by {self.user.first_name}"
    
class SavingFavorites(models.Model):
    advertisement = models.ForeignKey(Advertisement,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)