from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse, reverse_lazy
from .forms import *

current_user = User.objects.first()


class HomeView(ListView):
    model = Ad
    template_name = 'index.html'
    ordering = ['-creation_date']


class UserAdsView(ListView):
    model = Ad
    template_name = 'user-ads.html'

    def get_queryset(self):
        return Ad.objects.filter(user=User.objects.first()).order_by('-creation_date')


class AdInfoView(DetailView):
    model = Ad
    template_name = 'ad-info.html'


class AdCreateView(CreateView):
    model = Ad
    template_name = 'ad-create.html'
    form_class = AdForm
    success_url = reverse_lazy('user-ads')

    def form_valid(self, form):
        form.instance.user = User.objects.first()
        return super().form_valid(form)


class AdUpdateView(AdCreateView, UpdateView):
    template_name = 'ad-update.html'


class AdDeleteView(DeleteView):
    model = Ad
    template_name = 'ad-delete.html'
    success_url = reverse_lazy('user-ads')


