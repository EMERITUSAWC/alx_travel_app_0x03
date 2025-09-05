from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Booking


@shared_task
def send_booking_confirmation_email(booking_id):
    """
    Asynchronous task to send booking confirmation email.
    Triggered after a new booking is created.
    """
    try:
        booking = Booking.objects.get(id=booking_id)
        subject = "Booking Confirmation"
        message = (
            f"Hello {booking.user.username},\n\n"
            f"Your booking to {booking.destination} has been confirmed!\n"
            f"Booking ID: {booking.id}\n\n"
            "Thank you for choosing ALX Travel App!"
        )
        recipient = [booking.user.email]

        send_mail(
            subject,
            message,
            getattr(settings, "DEFAULT_FROM_EMAIL", "noreply@alxtravel.com"),
            recipient,
            fail_silently=False,
        )

        return f"Booking confirmation email sent to {booking.user.email} for booking {booking.id}"

    except Booking.DoesNotExist:
        return f"Booking with ID {booking_id} does not exist."
    except Exception as e:
        return f"Error sending booking confirmation email: {str(e)}"
