from django.db import models

# Create your models here.

class CustomUser(models.Model):
    id = models.AutoField(primary_key=True, default=None)
    name = models.CharField(max_length=128,default=None)
    email = models.EmailField(unique=True,default=None)
    password = models.CharField(max_length=128,default=None) 
    
    class Meta:
        db_table = 'Users' 
    
    def __str__(self):
        return self.email
    



class Trip(models.Model):
    trip_id=models.AutoField(primary_key=True)
    trip_name = models.CharField(max_length=100, default="Default Trip Name")
    email = models.EmailField(default="example@example.com")
    trip_from = models.CharField(max_length=100, default="Default From")
    trip_to = models.CharField(max_length=100, default="Default To")
    start_date = models.DateField(default=None)  # Set the default to the current date
    return_date = models.DateField(default=None)  # Set the default to the current date
    num_days = models.IntegerField(default=1)  # Set your desired default value
    accommodation_per_trip = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00)  # Set your desired default value
    num_trip_mates = models.PositiveIntegerField(default=5)  # Set your desired default value
    trip_description = models.TextField(default="Default Trip Description")

    class Meta:
        db_table = 'Trips'

    def __str__(self):
        return self.trip_name



class TripPhotos(models.Model):
    
    trip_image_id = models.AutoField(primary_key=True)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    trip_image = models.ImageField(upload_to='trip_images/', default='default_image.jpg')

    class Meta:
        db_table = 'Trip_images'