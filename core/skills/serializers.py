from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from core.skills.models import Fruit

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = ['name', 'description']

        