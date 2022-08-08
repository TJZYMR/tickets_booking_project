from django.core.mail import send_mail
from Movie_tickets_booking.settings import EMAIL_HOST_USER
from celery import shared_task


def send_mail_to(subject, message, receivers):
    send_mail(subject, message, EMAIL_HOST_USER, [receivers], fail_silently=False)


#! basic email making has been prepared,soin this email just get all the info of booking and send it to user in image format with ticket and qr code.
#! arguments=booking_id,user_id,movie,cinema,cinemahall,show,seats,total_amount,payment_mode,booking_status,show_start_time and end time,etcc...
@shared_task(name="send_mail_to")
def email_task_async(booking_id, user_email):
    subject = (
        "sending emails using celery for successful Booking of tickets and here is your booking id"
        + str(booking_id)
        # + str(user.username)
    )
    message = "Thank you"
    send_mail_to(subject, message, user_email)
