from django.db.models.signals import post_save, post_delete, pre_save # Importa os sinais pre_save, post_save e post_delete para conectar funções a eventos de salvamento e exclusão de modelos
from django.dispatch import receiver # Import the receiver decorator to connect signals to functions
from django.db.models import Sum
from .models import Car, CarInventory

def car_inventory_update():
    cars_count = Car.objects.all().count() # Conta o número total de carros no banco de dados
    cars_value = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value'] or 0.00 # Calcula a soma total dos valores dos carros, retornando 0.00 se não houver carros
    CarInventory.objects.create(
        cars_count=cars_count, 
        cars_value=cars_value
    ) # Cria um novo registro de CarInventory com o número total de carros e o valor total dos carros

@receiver(pre_save, sender=Car) # Conecta a função car_pre_save ao sinal pre_save do modelo Car, para que seja chamada antes de um carro ser salvo
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = f"{instance.brand} {instance.model} - {instance.model_year}" # Se o campo bio do carro estiver vazio, preenche-o com uma string formatada contendo a marca, modelo e ano do carro

@receiver(post_save, sender=Car) # Conecta a função car_post_save ao sinal post_save do modelo Car, para que seja chamada sempre que um carro for salvo
def car_post_save(sender, instance, **kwargs):
    car_inventory_update() 


@receiver(post_delete, sender=Car) # Conecta a função car_post_delete ao sinal post_delete do modelo Car, para que seja chamada sempre que um carro for deletado
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()