from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy

from webapp.forms import ChoiceForm
from webapp.models import Poll, Choice
from django.views.generic import CreateView, UpdateView, DeleteView


class ChoiceCreateView(CreateView):
    template_name = 'choice/choice_create.html'
    form_class = ChoiceForm
    model = Choice

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choice = form.save(commit=False)
        choice.poll = poll
        choice.save()
        return redirect('poll_view', pk=poll.pk)


class ChoiceUpdateView(UpdateView):
    template_name = 'choice/choice_update.html'
    form_class = ChoiceForm
    model = Choice

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})


class ChoiceDeleteView(DeleteView):
    template_name = 'choice/choice_delete.html'
    model = Choice

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})