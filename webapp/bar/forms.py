from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class FeedbackForm(forms.Form):
    first_name = forms.CharField(max_length=127)
    last_name = forms.CharField(max_length=127)
    email = forms.CharField(max_length=127)
    grade = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    like_design = forms.BooleanField(initial=False, required=False)
    like_functionality = forms.BooleanField(initial=False, required=False)
    like_content = forms.BooleanField(initial=False, required=False)
