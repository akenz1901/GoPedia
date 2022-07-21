from rest_framework import serializers

from gopedia_management.models import StudentSummarySubscriber
from django.contrib.auth import get_user_model


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSummarySubscriber
        fields = ('username', 'paid_user', 'list_of_course_code',
                  'last_date_purchased', 'number_of_purchased', 'vendor_names_and_number_purchased', 'email')


class UserAgentSerializer(serializers.ModelSerializer):
    list_of_available_courses = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('business_name',
                  'email',
                  'logo',
                  'list_of_available_courses')

    def get_list_of_available_courses(self, obj):
        return obj.get_list_of_available_courses()
