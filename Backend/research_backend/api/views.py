from django.contrib.auth.models import User
from .models import Research
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serialisers import UserSerialiser, ResearchSerialiser
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from pydantic import BaseModel


load_dotenv()

def research_query(statement):

    # llm1 = ChatOpenAI(model="gpt-4o-mini")
    llm2 = ChatAnthropic(model="claude-opus-4-20250514")

    result = llm2.invoke(statement)
    return (result.content)


# Create your views here.

class ResearchListCreate(generics.ListCreateAPIView):
    serializer_class = ResearchSerialiser
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        
        if Research.objects.all():
            change = Research.objects.all()[len(Research.objects.all())-1]
            change.research_papers = str(research_query(change.topic))
            change.save()
        else:
            print('Empty')

        

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

