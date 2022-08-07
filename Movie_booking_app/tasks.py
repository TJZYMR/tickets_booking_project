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


# from django.core.management import call_command


#! custome command called every 4 hours by celery worker
@shared_task
def deactivate_finished_shows():
    # logger.debug("celery preodical-background task started functioning for 1 min")
    # print("celery preodical-background task started functioning for 1 min")
    # print("celery background task started functioning for 1 min")
    # call_command("deactivate_finished_shows")
    # logger.debug("celery background task finished functioning for 1 min")
    # print("celery background task finished functioning for 1 min")
    # return "celery background task finished functioning for 1 min"/
    pass


from Movie_booking_app.models.show import Show
import datetime

from django.core.management import call_command  # NEW


@shared_task(name="print_msg_main")
def print_message(message, *args, **kwargs):
    # now = datetime.datetime.now()
    # expired_shows = Show.objects.filter(date__lt=now)
    # if expired_shows:
    #     for show in expired_shows:
    #         show.is_active = False
    #         show.save()
    #         for seat in CinemaHallSeat.objects.filter(
    #             cinema_hall_id=show.cinema_hall_id
    #         ):
    #             seat.state = SeatState.objects.get(id=1)
    #             seat.save()
    call_command(
        "delete_expired_shows",
    )


#!IMPORTANT
#! issue:one seat should have asssociated show with it.Here,seat woulbe be booked
#! for only one show.Therefore,every cinema hall seat should have associated show with it.
#!1=task
#! this task will be for running periodic task for every 3 hours to see
#! whether the show has ended successfully and if yes then all the seats of that
#! show occupies should be made empty.
# ?1.if the show is past and still has not deleted from shows,then user should not be able to book into it.
#! 2=task
#! making a queue for booking process so that every booking should be made after one is made.
#! so here we will be pushing booking request to queue.Celery task will get signal if
#! any new bookings,arrives and will do booking for that in FIFO manner.Here we will use
#! message queue(producer-consumer)(which has one-to-one relationship)

#! 3=task
#! how views be attached with redis cache so,improve performace.But this will be much
#! more be useful when the user searches for movie or anything like that.

#!3.9=task
#! make permissions or implement it using django available packages.
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

#!9=task
#! Making serializer class to return only specific fields of use.

#!10=task
#! make json schema for only booking api

#!11=task
#! web scraper for fething news for specific movie and actor.

#!12=task
#! Integrating Mongodb in this project tottaly for data fetching.

#!13=task
#! Integrating elasticsearch in this project tottaly for data fetching.

#!14=task
#! How to use boto3 and give this to django task.
# ?R&Ds:
# 1)which to use Rabbitmq or Kafka for message queueing?
# 2)which to use redis or memcached for caching?
# 3)which to use celery or asyncio for background tasks?
# 4)which to use celerybeat or cron for periodic tasks?
# 5)what fields should be included in the database for ml task of recommendation?
# 6)How big data tools like spark or hadoop can be utilised here and in what manner?
# 7)How to make a recommendation system using machine learning?
# 8)Where varnish and ELK stack can be utilised here?
# 9)Side task should be to learn hadoop or spark from the data from our
# 10)see flower documentation for more information about new things.
