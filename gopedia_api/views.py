from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentsSerializer
from gopedia_management.models import StudentSummarySubscriber


@api_view(['GET', 'POST'])
def create_student(request):
    if request.method == 'GET':
        students = StudentSummarySubscriber.objects.all()
        serializer = StudentsSerializer(students, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH', 'GET'])
def update_student_purchase(request, email):
    try:
        student = StudentSummarySubscriber.objects.get(email__exact=email)
    except StudentSummarySubscriber.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentsSerializer(student)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = StudentsSerializer(student, data=request.data)

        if serializer.is_valid():
            student.change_recent_purchase()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        serializer = StudentsSerializer(student, data=request.data, partial=True)

        if serializer.is_valid():
            student.change_recent_purchase()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)