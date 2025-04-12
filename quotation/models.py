from django.db import models
from django.core.validators import MinValueValidator



class Product(models.Model):
    usage_location_list = [
        ('' , " "),
        ('kitchen', 'KITCHEN'),
        ('laundry', 'LAUNDRY ROOM'),
        ('living_room', 'LIVING ROOM'),
        ('bathroom', 'BATHROOM'),
        ('office', 'OFFICE'),        
    ]

    usage_location = models.CharField(max_length=50, choices=usage_location_list, blank=True)
    prod_category = models.CharField(max_length=255, blank=True)
    prod_type = models.CharField(max_length=255, blank=True)
    prod_name = models.CharField(max_length=255, blank=False, null=False)

    desc = models.TextField()
    stock = models.PositiveBigIntegerField()
    price = models.DecimalField(max_digits = 7, decimal_places = 2,  validators=[MinValueValidator(0.00)])
    date_added = models.DateTimeField(auto_now_add = True)
    picture = models.ImageField(upload_to='product_images/')


    def __str__(self):
        return self.prod_name
