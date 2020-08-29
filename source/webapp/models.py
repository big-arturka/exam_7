from django.db import models


class Poll(models.Model):
    question = models.TextField(max_length=2000, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return "{}. {}".format(self.pk, self.question)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'