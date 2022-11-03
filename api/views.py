from api.models import Aluno
from api.serializers import AlunoSerializer

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    permission_classes = []
    #
    # def create(self, request, *args, **kwargs):
    #     print(request.data)
    #     # print()
    #     aluno = Aluno(nome=request.data['nome'][0], documento=request.data['documento'].read())
    #     aluno.save()
    #     return Response({})