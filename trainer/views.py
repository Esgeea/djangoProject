from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from trainer.filters import TrainerFilter
from trainer.forms import TrainerForm, TrainerUpdateForm
from trainer.models import Trainer


class TrainerCreateView(LoginRequiredMixin, CreateView):
    template_name = 'trainer/create_trainer.html'
    model = Trainer
    form_class = TrainerForm
    success_url = reverse_lazy('home_page')


class TrainerListView(LoginRequiredMixin, ListView):
    template_name = 'trainer/list_of_trainers.html'
    model = Trainer
    context_object_name = 'all_trainers'

    def get_queryset(self):
        return Trainer.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        trainers = Trainer.objects.filter(active=True)
        myFilter = TrainerFilter(self.request.GET, queryset=trainers)
        trainers = myFilter.qs
        data['all_trainers'] = trainers
        data['filters'] = myFilter.form

        return data


class TrainerUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'trainer/update_trainer.html'
    model = Trainer
    form_class = TrainerUpdateForm
    success_url = reverse_lazy('list-trainers')


class TrainerDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'trainer/delete_trainer.html'
    model = Trainer
    success_url = reverse_lazy('list-trainers')


class TrainerDetailView(LoginRequiredMixin, DetailView):
    template_name = 'trainer/details_trainer.html'
    model = Trainer