from django.urls import path
from . import views


urlpatterns = [
    path('', views.feedback_home, name='feedback_home'),
    path("feedback-success/", views.feedback_success, name="feedback-success")
]
