from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path("feedback-success/", views.feedback_success, name="feedback-success"),
    path("404/", views.not_found, name="404")
]
