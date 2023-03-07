from django.shortcuts import render
from .models import Activity
from .serializers import ActivitySerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class ActivityListAPI(APIView):
    def get(self, request):
        queryset = Activity.objects.all()
        print(queryset)
        serializer = ActivitySerializer(queryset, many=True)
        return Response(serializer.data)