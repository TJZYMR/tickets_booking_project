from django.db import models
from Movie_booking_app.models.movie import Movie

from Movie_booking_app.models.statuses import PaymentStatus
from Movie_booking_app.models.users import User


class Coupen(models.Model):
    code = models.CharField(max_length=10)
    discount = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code


class PaymentMode(models.Model):
    """
    Payment mode model
    """

    payment_mode = models.CharField(max_length=20)

    def __str__(self):
        return self.payment_mode

    class Meta:
        verbose_name_plural = "Payment Modes"


class Payment(models.Model):
    """
    Payment model
    """

    payment_type = models.ForeignKey(PaymentMode, on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_time = models.TimeField()
    payment_status = models.ForeignKey(PaymentStatus, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=20)
    payment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    payment_coupon = models.ForeignKey(
        Coupen, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.payment_type

    class Meta:
        verbose_name_plural = "Payments"
