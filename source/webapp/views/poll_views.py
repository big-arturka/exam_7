from django.urls import reverse, reverse_lazy

from webapp.forms import PollForm, ChoiceForm
from webapp.models import Poll, Choice, Answer
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView


class IndexView(ListView):
    template_name = 'poll/index.html'
    context_object_name = 'polls'
    paginate_by = 5
    paginate_orphans = 2

    def get_queryset(self):
        return Poll.objects.all().order_by('-created_at')


class PollView(DetailView):
    template_name = 'poll/poll_view.html'
    model = Poll

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        choices = self.object.choices.all()

        answer_count = Answer.objects.filter(poll_id=self.kwargs.get('pk')).count()
        ans_dict = {}
        for i in Answer.objects.filter(poll_id=self.kwargs.get('pk')):
            key = i.variant.pk
            if key in ans_dict:
                ans_dict[key] += 1
            else:
                ans_dict[key] = 1

        for i in ans_dict:
            ans_dict[i] = ans_dict[i] / answer_count * 100

        context['percents'] = ans_dict
        context['answer_count'] = answer_count
        context['choices'] = choices
        context['form'] = ChoiceForm()

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
