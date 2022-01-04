from django.contrib.auth.models import User
from rest_framework import  viewsets
from core.skills.models import Fruit

from core.skills.serializers import FruitSerializer, UserSerializer

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FruitViewSet(viewsets.ModelViewSet):
    queryset = Fruit.objects.all()
    # Select *from fruits;
    serializer_class = FruitSerializer