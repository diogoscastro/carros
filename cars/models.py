from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=20, blank=True, null=True)
    value = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.model_year})"