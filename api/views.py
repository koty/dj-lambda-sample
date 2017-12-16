
# from django.db import transaction
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api.models import AccessKey, User
from api.serializers import UserSerializer, AccessKeySerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class MigrateView(APIView):
    def get(self, request):
        from django.core import management
        management.call_command('migrate')
        return Response({})
