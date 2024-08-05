from django.db import models




# Create your models here.
class Contact(models.Model):
     
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     phone= models.CharField(max_length=13)
     email= models.CharField(max_length=100)
     content= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

     def _str_(self):
          return 'Message from'+self.name+' - '+self.email


# models.py
from django.db import models

class Concert(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    trailer_url = models.URLField()
    timings = models.DateTimeField()
    artists = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Booking(models.Model):
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    contact_no = models.CharField(max_length=15)
    num_of_people = models.IntegerField()

    # Add other fields as needed
    card_number = models.CharField(max_length=16, verbose_name="Card Number")
    card_expiry = models.CharField(max_length=4, verbose_name="Card Expiry")
    card_cvc = models.CharField(max_length=3, verbose_name="Card CVC")
    card_name = models.CharField(max_length=255, verbose_name="Card Holder Name")
    def __str__(self):
        return f'Message from {self.username} - {self.email}'



    
    

   

    



