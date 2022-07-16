from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.create_student, name='create student'),
    path('student/<email>/', views.update_student_purchase, name='Fetch, Remove or Modify a student')
]
