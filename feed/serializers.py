from rest_framework import serializers
from .models import Feed

class FeedSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Feed        # user 모델 사용
        fields = '__all__'            # 모든 필드 포함