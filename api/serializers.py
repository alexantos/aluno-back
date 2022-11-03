from api.models import *
from rest_framework import serializers


class AlunoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'url', 'nome', 'documento']