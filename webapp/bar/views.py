from django.shortcuts import render
from django.http import HttpResponse
from . import models
from . import forms


def index(request):
    data = {
        'title': 'Меню бара',
        'values': ['Закуски', 'Пицца', 'Алкоголь', 'Свежевыжатые соки', 'Кальяны'],
    }
    return render(request, 'bar/index.html', data)


def about(request):
    data = {
        'info': {
            'Имя': 'Кирилл',
            'Возраст': '20',
            'Университет': 'ИТМО',
            'Факультет': 'ИКТ'
        }
    }
    return render(request, 'bar/about.html', data)


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

    return render(request, "feedback-success.html")


def not_found(request, exception=None):
    return render(request, "not_found.html")