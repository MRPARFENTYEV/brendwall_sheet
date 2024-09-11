from django.contrib.auth.management.commands.changepassword import UserModel
from rest_framework import serializers
from brandwall_test_app.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title','description','price']



