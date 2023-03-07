from django.shortcuts import render
from .serializers import FeedSerializer
from .models import Feed
from rest_framework.response import Response
from rest_framework.views import APIView

class FeedListAPI(APIView):
    def get(self, request):
        queryset = Feed.objects.all()
        print(queryset)
        serializer = FeedSerializer(queryset, many=True)
        return Response(serializer.data)
    
