from django.db import models


class Poll(models.Model):
    question = models.TextField(max_length=2000, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return "{}. {}".format(self.pk, self.question)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Choice(models.Model):
    variant = models.TextField(max_length=2000, verbose_name='Вариант ответа')
    poll = models.ForeignKey('webapp.Poll', related_name='choices', on_delete=models.CASCADE, verbose_name='Вопрос')

    def __str__(self):
        return "{}. {}".format(self.pk, self.variant)

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'


class Answer(models.Model):
    poll = models.ForeignKey('webapp.Poll', related_name='answer_poll', on_delete=models.CASCADE, verbose_name='Вопрос')
    variant = models.ForeignKey('webapp.Choice', related_name='answer_choice',
                                on_delete=models.CASCADE, verbose_name='Вариант')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return "{}. {}-{}".format(self.pk, self.poll, self.variant)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
