from rest_framework.serializers import ModelSerializer 
from .models import Logo

class LogoSerializer(ModelSerializer):
    class Meta:
        model = Logo 
        fields = '__all__'