from django.urls import path
from . import views


urlpatterns =[
    path('research/', views.ResearchListCreate.as_view(), name='research-list'),
    path('research/delete/<int:pk>/', views.ResearchDelete.as_view(), name='delete-note'),
]