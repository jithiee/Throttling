from django.shortcuts import render
from rest_framework import viewsets
from . models import Teachers
from . serializer import TeacherSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttling import JackThrottel

class TeacherModelViewApi(viewsets.ModelViewSet):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # throttle_classes = [AnonRateThrottle,UserRateThrottle]
    throttle_classes = [AnonRateThrottle,JackThrottel]
    
