from rest_framework import serializers
from .models import Escalas

class EscalasSerializers(serializers.ModelSerializer):

    class Meta:

        model = Escalas
        fields = '__all__'