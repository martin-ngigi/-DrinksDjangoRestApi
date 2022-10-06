# from python to json
from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Drink
        #feilds = ['id', 'name', 'description']
        fields = '__all__'