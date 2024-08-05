from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Booking

@receiver(post_save, sender=Booking)
def send_booking_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Thank You for Booking',
            'Your tickets are booked. Thank you for visiting!',
            'from@example.com',
            [instance.email],
            fail_silently=False,
        )
