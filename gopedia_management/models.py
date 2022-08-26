from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import os


class PdfAdmin(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    business_name = models.CharField(max_length=250, blank=True, null=True, unique=True)
    pdf_file = models.FileField(verbose_name="summary", upload_to="static/", null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now())
    logo = models.ImageField(upload_to="media/", blank=True, null=True)

    def __str__(self):
        return self.business_name

    def get_list_of_available_courses(self):
        if len(os.getcwd()) > 7:
            path = f'{os.getcwd()}\\gopedia_management\\static\\{self.business_name}'
        else:
            path = f'{os.getcwd()}/gopedia_management/static/{self.business_name}'
        try:
            list_of_available_courses = os.listdir(path)
            new_list = []
            for i in list_of_available_courses:
                file_url = f'https://gopediacdn.herokuapp.com/static/{self.business_name}/'
                new_list.append(file_url + i)
            return new_list
        except FileNotFoundError:
            return []


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
