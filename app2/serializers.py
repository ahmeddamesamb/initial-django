from rest_framework import serializers

from .models import Client
from .models import Drink
from .models import Gestionaire
from .models import Livreur


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = '__all__'


class GestionaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gestionaire
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class LivreurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livreur
        fields = '__all__'
