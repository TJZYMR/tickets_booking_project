from django.db import models

# Create your models here.
class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# def email_schedule(mail, pk):
#     print("email schedule")
#     email_task_async.delay(mail, pk)
