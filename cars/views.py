from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView


# CRUD
# Views como classe:

class CarsListView(ListView):
    model = Car
    template_name = "cars.html"
    context_object_name = "cars"

    def get_queryset(self):
        cars = super().get_queryset().order_by("model")  # Ordena os carros por modelo
        search = self.request.GET.get("search") # Busca

        if search:
            cars = cars.filter(model__icontains=search)  # Filtra os carros pelo modelo, usando uma busca case-insensitive
        return cars  # Retorna a queryset de carros filtrada para ser usada no template


class newCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = "new_car.html"
    success_url = "/cars/"  # Redireciona para a lista de carros após criar um novo carro


class CarDetailView(DetailView):
    model = Car
    template_name = "car_detail.html"


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = "car_update.html"
    success_url = "/cars/"  # Redireciona para a lista de carros após editar um carro