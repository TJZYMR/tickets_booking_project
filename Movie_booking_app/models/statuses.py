from django.db import models


class SeatState(models.Model):
    seat_state = models.CharField(max_length=100)

    def __str__(self):
        return self.seat_state


class PaymentStatus(
    models.Model
):  # create unpaid,pending,completed,failed,declined,cencelled,abandoned,settling,settled,refunded
    payment_status = models.CharField(max_length=100)

    def __str__(self):
        return self.payment_status

    class Meta:
        # verbose_name = "Payment-Status"
        verbose_name_plural = "Payment-Status"


class BookingStatus(
    models.Model
):  # requested,Pending,Confirmed,Checked-in,Cancelled,Abandoned
    booking_status = models.CharField(max_length=100)

    def __str__(self):
        return self.booking_status

    class Meta:
        verbose_name_plural = "Booking-Status"


class AccountStatus(models.Model):  # active,closed,cancelled,black-listed,blocked
    account_status = models.CharField(max_length=100)

    def __str__(self):
        return self.account_status

    class Meta:
        verbose_name_plural = "Account-Status"
