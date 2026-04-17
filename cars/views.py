from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.views import View


# Views como funções:

# # cars
# def cars_view(request):
#     cars = Car.objects.all().order_by("model")  
#     search = request.GET.get("search")  
#         cars = cars.filter(model__icontains=search)  case-insensitive
#     return render(request, "cars.html", {"cars": cars}) 

# # new_car
# def new_cars_view(request):
#     if request.method == "POST":
#         new_car_form = CarModelForm(request.POST, request.FILES) 
#         if new_car_form.is_valid():  
#             new_car_form.save()  
#             return redirect("cars_list")  
#     else:
#         new_car_form = CarModelForm()  
#     return render(request, "new_car.html", {"new_car_form": new_car_form}) 


# Views como classe:

class CarsView(View):

    def get(self, request):
        cars = Car.objects.all().order_by("model")  # Ordena os carros por data de criação
        search = request.GET.get("search")  # Obtém o valor do parâmetro de busca da URL
        if search:
            cars = cars.filter(model__icontains=search)  # Filtra os carros pelo modelo, usando uma busca case-insensitive
        return render(request, "cars.html", {"cars": cars}) # Renderiza o template "cars.html" e passa a lista de carros filtrada como contexto para o template


class NewCarView(View):

    def get(self, request):
        new_car_form = CarModelForm()  
        return render(request, "new_car.html", {"new_car_form": new_car_form})
    
    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES) # Recebe os Dados e Arquivos do formulário
        if new_car_form.is_valid():  # Verifica se o formulário é válido
            new_car_form.save()  # Salva o novo carro no banco de dados se for válido
            return redirect("cars_list")  # Redireciona para a lista de carros após salvar o novo carro
        return render(request, "new_car.html", {"new_car_form": new_car_form})
    
    