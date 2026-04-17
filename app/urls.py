from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import CarsListView, newCarCreateView, CarDetailView, CarUpdateView
from accounts.views import register_view, login_view, logout_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("cars/", CarsListView.as_view(), name="cars_list"),
    path("new_car/", newCarCreateView.as_view(), name="new_car"),
    path("car/<int:pk>/", CarDetailView.as_view(), name="car_detail"),  # URL para a página de detalhes de um carro, usando o ID do carro <int:pk>
    path("car/<int:pk>/update/", CarUpdateView.as_view(), name="car_update"),  # URL para a página de edição de um carro, usando o ID do carro <int:pk>
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Adiciona as URLs para servir arquivos de mídia durante o desenvolvimento, usando as configurações MEDIA_URL e MEDIA_ROOT do settings.py
