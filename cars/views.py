from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from cars.models import Car
from cars.forms import CarModelForm
  
class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model', 'brand', 'factory_year')
        search = self.request.GET.get('search')
        brand = self.request.GET.get('brand')
        factory_year = self.request.GET.get('factory_year')

        if search:
            cars = cars.filter(model__icontains=search)
        
        if brand:
            cars = cars.filter(brand__icontains=brand)

        if factory_year:
            cars = cars.filter(factory_year=int(factory_year))
        return cars
class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    context_object_name = 'car'

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = reverse_lazy('cars_list')

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})
    
@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = reverse_lazy('cars_list')