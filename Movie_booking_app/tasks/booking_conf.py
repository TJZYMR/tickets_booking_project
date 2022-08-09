from io import BytesIO
from django.core.mail import send_mail
from Movie_booking_app.models.statuses import PaymentStatus
from Movie_tickets_booking.settings import EMAIL_HOST_USER
from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from io import BytesIO
from django.template.loader import get_template

from xhtml2pdf import pisa


def send_mail_to(subject, message, receivers):
    send_mail(subject, message, EMAIL_HOST_USER, [receivers], fail_silently=False)


#! basic email making has been prepared,so in this email just get all the info of booking and send it to user in image format with ticket and qr code.
#! arguments=booking_id,user_id,movie,cinema,cinemahall,show,seats,total_amount,payment_mode,booking_status,show_start_time and end time,etcc...
@shared_task(name="send_mail_to")
def email_task_async(booking_id, user_email, payment_status, ticket_info):
    if payment_status == PaymentStatus.objects.get(id=2).id:
        subject = (
            "sending emails using celery for cancelling of the tickets and payment"
            + str(booking_id)
        )
        message = "Cancelled"
        send_mail_to(subject, message, user_email)
    elif payment_status == PaymentStatus.objects.get(id=3).id:
        context = {
            "user": ticket_info["user"],
            "movie": ticket_info["movie"],
            "cinema": ticket_info["cinema"],
            "cinemahall": ticket_info["cinemahall"],
            "show": ticket_info["show"],
            "show_time": ticket_info["show"],
            # "seats": ticket_info.seats,
        }
        subject = (
            "sending emails using celery for successful Booking of tickets and here is your booking id"
            + str(booking_id)
        )
        template = get_template("ticket.html")
        html = template.render(context)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
        if not pdf.err:
            p = result.getvalue()

        email_message = EmailMultiAlternatives(
            to=(user_email,),
            subject=subject,
            body="Your E-ticket",
        )
        filename = "E-ticket.pdf"
        mimetype_pdf = "application/pdf"
        email_message.attach(filename, p, mimetype_pdf)
        email_message.send()  # TODO zzz mabye change this to Tru


# def create_pdf():
#     context = {
#         "name": "Hello",
#     }
#     html_string = render_to_string("ticket.html", context)
#     html = HTML(string=html_string)
#     buffer = io.BytesIO()
#     html.write_pdf(target=buffer)
#     pdf = buffer.getvalue()

#     email_message = EmailMultiAlternatives(
#         to=("youremailadress@gmail.com",),
#         subject="subject test print",
#         body="heres is the body",
#     )
#     filename = "E-ticket.pdf"
#     mimetype_pdf = "application/pdf"
#     email_message.attach(filename, pdf, mimetype_pdf)
#     email_message.send(fail_silently=False)  # TODO zzz mabye change this to Tru
