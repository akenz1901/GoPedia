from rest_framework import serializers

from gopedia_management.models import StudentSummarySubscriber


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSummarySubscriber
        fields = ('username', 'paid_user', 'list_of_course_code',
                  'last_date_purchased', 'number_of_purchased', 'vendor_names_and_number_purchased', 'email')
