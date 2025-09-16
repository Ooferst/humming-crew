import uuid
from django.db import models

class Products(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('shoes', 'Shoes'),
        ('pants', 'Pants'),
        ('jacket', 'Jacket'),
        ('bag', 'Sports Bag'),
        ('accessory', 'Accessory'),
    ]

    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('N/A', 'Not Applicable'),  # untuk barang tanpa size
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    size = models.CharField(max_length=3, choices=SIZE_CHOICES, default='N/A')
    views = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='jersey')
    stocks = models.PositiveIntegerField(default=0)
    thumbnail = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.category})"
    
    @property
    def is_products_hot(self):
        return self.views > 20
        
    def increment_views(self):
        self.views += 1
        self.save()
