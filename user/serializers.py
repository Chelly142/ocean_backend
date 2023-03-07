from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = User        # user 모델 사용
        fields = '__all__'            # 모든 필드 포함