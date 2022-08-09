from __future__ import absolute_import, unicode_literals

from Movie_booking_app.models.book import Booking
from Movie_booking_app.models.cinemahallseat import CinemaHallSeat, ShowWiseSeats
from Movie_booking_app.models.statuses import BookingStatus, PaymentStatus, SeatState
import logging


logger = logging.getLogger(__name__)


from django.core.management import call_command  # NEW
from celery import shared_task

#! custome command called every 4 hours by celery worker
@shared_task(name="print_msg_main")
def print_message(message, *args, **kwargs):
    call_command(
        "delete_expired_shows",
    )


@shared_task
def seat_timeout(seats, booking_id, show_id):
    logger.debug("celery background task started functioning for 1 min")
    print(
        seats, booking_id
    )  # !celery will not recognize it as it does not have control over the terminal,u know async process
    payment_pending = PaymentStatus.objects.get(id=1)
    book_cancelled = BookingStatus.objects.get(id=2)
    payment_cancelled = PaymentStatus.objects.get(id=2)
    if Booking.objects.get(id=booking_id).payment_status == payment_pending:
        Booking.objects.filter(id=booking_id).update(
            payment_status=payment_cancelled, booking_status=book_cancelled
        )
        for seat in ShowWiseSeats.objects.filter(
            cinema_hall_seat_id__in=seats, show_id=show_id
        ):
            seat.state_id = SeatState.objects.get(id=3)
            seat.save()
    logger.debug("celery background task finished functioning for 1 min")
