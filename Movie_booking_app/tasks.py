from __future__ import absolute_import, unicode_literals
from celery import shared_task
from Movie_booking_app.models.book import Booking
from Movie_booking_app.models.cinemahallseat import CinemaHallSeat
from Movie_booking_app.models.statuses import BookingStatus, PaymentStatus, SeatState
import logging

logger = logging.getLogger(__name__)


@shared_task
def seat_timeout(seats, booking_id):
    logger.debug("celery background task started functioning for 1 min")
    print(
        seats, booking_id
    )  # !celery will not recognize it as it doe not ave control over the terminal,u know async process
    payment_pending = PaymentStatus.objects.get(id=2)
    book_cancelled = BookingStatus.objects.get(id=5)
    payment_cancelled = PaymentStatus.objects.get(id=4)
    if Booking.objects.get(id=booking_id).payment_status == payment_pending:
        Booking.objects.filter(id=booking_id).update(
            payment_status=payment_cancelled, booking_status=book_cancelled
        )
        for seat in CinemaHallSeat.objects.filter(id__in=seats):
            seat.state = SeatState.objects.get(id=1)
            seat.save()
    logger.debug("celery background task finished functioning for 1 min")


#!1=task
#! this task will be for running periodic task for every 3 hours to see
#! whether the show has ended successfully and if yes then all the seats of that
#! show occupies should be made empty.

#! 2=task
#! making a queue for booking process so that every booking should be made after one is made.
#! so here we will be pushing booking request to queue.Celery task will get signal if
#! any new bookings,arrives and will do booking for that in FIFO manner.Here we will use
#! message queue(producer-consumer)(which has one-to-one relationship)

#! 3=task
#! how views be attached with redis cache so,improve performace.But this will be much
#! more be useful when the user searches for movie or anything like that.

#! 4=task
#! home page will contain the recommendation from the ai/ml part.

#! 5=task
#! subscribed user should get notification using pub-sub system of available seats.

#! 6=task
#! when the payment_status is paid,the signal should be made to start task of sending
# ! mail to the user who booked in image or pdf format with qr made by you.

#! 7=task
#! razorpay third party payment gateway integration needs to be made and after payment the
#! payment_status should be updated in the database.

#! 8=task
#! for cancelling the seats reservation,the signal should be made to start task of
#! emptying the seats of the users and send mail that the reservation was cancelled successfully.


# ?R&Ds:
# 1)which to use Rabbitmq or Kafka for message queueing?
# 2)which to use redis or memcached for caching?
# 3)which to use celery or asyncio for background tasks?
# 4)which to use celerybeat or cron for periodic tasks?
# 5)what fields should be included in the database for ml task of recommendation?
# 6)How big data tools like spark or hadoop can be utilised here and in what manner?
