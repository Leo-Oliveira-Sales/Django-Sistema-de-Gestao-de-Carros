from django.db import models

# Criando a Tabela.


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name # Vai retornar o nome da marca, e não mais Brand object (1), Brand object (2) etc.

# blank=True permite que o campo seja deixado em branco, null=True permite que o campo seja nulo.
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand') # ForeignKey é um campo de chave estrangeira, on_delete=models.PROTECT impede que a marca seja deletada se houver um carro associado a ela, related_name é o nome do relacionamento.
    factory_year = models.IntegerField(blank=True, null=True) 
    model_year = models.IntegerField(blank=True, null=True) 
    plate = models.CharField(max_length=10, blank=True, null=True) 
    value = models.FloatField(blank=True, null=True) 
    photo = models.ImageField(upload_to='cars/', blank=True, null=True) # ImageField é um campo de imagem, upload_to é o diretório onde as imagens serão armazenadas
    bio = models.TextField(blank=True, null=True) # TextField é um campo de texto, ideal para descrições mais longas. DESCRIÇÃO DO CARRO

    def __str__(self):
        return self.model # Vai retornar o nome do modelo do carro, e não mais Car object (1), Car object (2) etc.


class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add=True define que o campo será preenchido automaticamente com a data e hora atual quando o objeto for criado.

    class Meta:
        ordering = ['-created_at'] # Ordena os objetos por data de criação, do mais recente para o mais antigo/decrescente.

    def __str__(self):
        return f"{self.cars_count} - {self.cars_value}" # Vai retornar a quantidade de carros e o valor total do inventário, por exemplo: "10 - 50000.0".