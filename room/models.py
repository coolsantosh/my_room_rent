from django.db import models
from account.models import User


ROOM_TYPE_CHOICES=[
    ('Single','Single'),
    ('Double','Double')
]

DISTRICT_CHOICE=[
    ('Kathmandu','Kathmandu'),
    ('Pokhara','Pokhara')
]

STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Not Available', 'Not Available'),
    ]

# Create your models here.
class Room(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPE_CHOICES)
    size = models.IntegerField(help_text='Size in square feet')
    amenities = models.TextField(blank=True, null=True)
    rent_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Available')
    is_available = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='room_images/', blank=True, null=True)

    # Address
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100,choices=DISTRICT_CHOICE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.room_type}"

    def get_full_address(self):
        return f"{self.district} {self.city}"
