from django.urls import path
from . import views

urlpatterns = [
    path('course/', views.course_detail, name='course_detail'),
    path('submit/<int:question_id>/', views.submit_exam, name='submit_exam'),
]
