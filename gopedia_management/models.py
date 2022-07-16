from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class PdfAdmin(AbstractUser):
    email = models.EmailField(unique=True)
    pdf_file = models.FileField(verbose_name="summary", upload_to="static/", null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now())


class StudentSummarySubscriber(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=150, unique=True, null=False, blank=False)
    paid_user = models.BooleanField(default=False)
    list_of_course_code = ArrayField(models.CharField(max_length=30), verbose_name="course codes", size=14)
    date_joined = models.DateTimeField(auto_created=True, auto_now=True)
    last_date_purchased = models.DateTimeField(verbose_name="Recent purchase date", default=timezone.now())
    number_of_purchased = models.SmallIntegerField(default=0)
    vendor_names_and_number_purchased = models.JSONField(null=True, default={'Calculus': 0, 'Winsmart': 0, "Jblack": 0})

    def change_recent_purchase(self):
        self.last_date_purchased = timezone.now()
        self.save()

    def __str__(self):
        return self.username
