from django.db.models.signals import post_save, post_delete, pre_save, pre_delete
from django.dispatch import receiver # Import the receiver decorator to connect signals to functions
from .models import Car

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    print(f"O carro {instance} será cadastrado.")

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    print(f"O carro {instance} foi cadastrado.")
@receiver(pre_delete, sender=Car)
def car_pre_delete(sender, instance, **kwargs):
    print(f"O carro {instance} está prestes a ser excluído.")

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    print(f"O carro {instance} foi excluído.")