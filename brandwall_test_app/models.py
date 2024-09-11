from django.db import models
from django.core.validators import MinValueValidator


# API (Django):
# Создайте модель продукта с полями: название (строка), описание (текст), цена (десятичное число).

class Product(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False, error_messages={'required': 'Это поле не может быть пустым'})
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(validators=[MinValueValidator(1, message='похоже потребуется ввести число побольше')])

    def __str__(self):
        return self.title

    def return_price(self):
        return self.price

# Создайте модель продукта с полями: название (строка), описание (текст), цена (десятичное число).
