from django.shortcuts import render
from . import models
from . import forms


def feedback_home(request):
    return render(request, 'feedback/feedback_home.html')


def feedback_success(request):
    form = forms.FeedbackForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        feedback = models.Feedback(
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            grade=data["grade"],
            like_design=data.get("like_design"),
            like_functionality=data.get("like_functionality"),
            like_content=data.get("like_content")
        )
        feedback.save()

    return render(request, "feedback/feedback-success.html")


def not_found(request, exception=None):
    return render(request, "not_found.html")
