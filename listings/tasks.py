from alx_travel_app.celery_app import app

@app.task
def send_booking_confirmation_email(booking_id):
    # Replace this print with actual email logic
    print(f"Sending booking confirmation email for booking ID: {booking_id}")
    return True

