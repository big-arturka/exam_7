from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View

from webapp.models import Poll, Answer, Choice


class AnswerView(View):
    def get(self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choices = poll.choices.all()
        context = {
            'poll': poll,
            'choices': choices
        }
        return render(request, 'answer/answer.html', context)

    def post(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        variant = get_object_or_404(Choice, pk=request.POST.get('answer'))
        if 'answers':
            Answer.objects.create(poll=poll, variant=variant)
        return redirect('index')
