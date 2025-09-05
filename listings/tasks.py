from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_confirmation_email(booking_id, user_email):
    subject = "Booking Confirmation"
    message = f"Your booking with ID {booking_id} was successful!"
    send_mail(subject, message, "noreply@travelapp.com", [user_email])
    return f"Confirmation email sent to {user_email}"
