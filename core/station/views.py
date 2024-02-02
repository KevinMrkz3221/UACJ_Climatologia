from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Station
from .forms import StationForm
# Create your views here.


class StationListView(LoginRequiredMixin, ListView):
    template_name='estacion/estaciones_list.html'
    model = Station
    context_object_name = 'estaciones'

    login_url='/account/sign-in'

class StationCreateView(LoginRequiredMixin, CreateView):
    template_name = 'estacion/estacion_create.html'
    model = Station
    form_class = StationForm

    success_url = '/estaciones/listado'
    login_url = '/account/sign-in'

class StationDetailView(LoginRequiredMixin, DetailView):
    template_name = 'estacion/estacion_detail.html'
    model = Station
    context_object_name = 'estacion'


    login_url = '/account/sign-in'


class StationDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'estacion/estacion_delete.html'
    model = Station
    context_object_name = 'estacion'


    success_url = '/estaciones/listado'
    login_url = '/account/sign-in'

class StationUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'estacion/estacion_create.html'
    model = Station
    form_class = StationForm
    context_object_name = 'estacion'

    success_url = '/estaciones/listado'
    login_url = '/account/sign-in'


