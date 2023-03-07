from rest_framework import serializers
from .models import Activity


class ActivitySerializer(serializers.ModelSerializer) :
    class Meta :
        model = Activity        # user 모델 사용
        fields = '__all__'            # 모든 필드 포함