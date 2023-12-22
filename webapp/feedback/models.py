from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Feedback(models.Model):
    first_name = models.CharField('Имя', max_length=127)
    last_name = models.CharField('Фамилия', max_length=127)
    email = models.CharField('Электронная почта', max_length=127)
    grade = models.IntegerField('Рейтинг', validators=[MinValueValidator(1), MaxValueValidator(5)])
    like_design = models.BooleanField(default=False)
    like_functionality = models.BooleanField(default=False)
    like_content = models.BooleanField(default=False)

    def __str__(self):
        return f'Почта: {self.email}'

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
