from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from .models import Feed
from rest_framework.views import APIView
from .serializers import FeedSerializer
class FeedListAPI(APIView):
    def get(self, request):
        queryset = Feed.objects.all()
        print(queryset)
        serializer = FeedSerializer(queryset, many=True)
        return Response(serializer.data)