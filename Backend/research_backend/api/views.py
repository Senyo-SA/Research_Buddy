from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Research
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serialisers import UserSerialiser, ResearchSerialiser


# Create your views here.

class ResearchListCreate(generics.ListCreateAPIView):
    serializer_class = ResearchSerialiser
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Research.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)



class ResearchDelete(generics.DestroyAPIView):
    serializer_class = ResearchSerialiser
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Research.objects.filter(author=user)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser
    permission_classes = [AllowAny]

