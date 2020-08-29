from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy

from webapp.forms import PollForm
from webapp.models import Poll, Choice
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView


class IndexView(ListView):
    template_name = 'poll/index.html'
    context_object_name = 'polls'
    paginate_by = 5
    paginate_orphans = 2
    ordering = ['-created_at']

    def get_queryset(self):
        return Poll.objects.all()


class PollView(DetailView):
    template_name = 'poll/poll_view.html'
    model = Poll

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        choices = self.object.choices.all()
        context['choices'] = choices

        return context


class PollCreateView(CreateView):
    template_name = 'poll/poll_create.html'
    form_class = PollForm
    model = Poll

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollUpdateView(UpdateView):
    template_name = 'poll/poll_update.html'
    form_class = PollForm
    model = Poll

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollDeleteView(DeleteView):
    template_name = 'poll/poll_delete.html'
    model = Poll
    success_url = reverse_lazy('index')