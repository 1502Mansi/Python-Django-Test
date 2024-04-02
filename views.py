from django.shortcuts import render
from rest_framework import generics
from .models import Users
from .serializer import UsersSerializer

#create clients and display them
class CreateUsersList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

#retrieve, update or delete clients by id
class RetrieveUpdateDeleteUsers(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


from django.shortcuts import render
from rest_framework import generics
from .models import Clients
from .serializer import ClientsSerializer


#create your views here.

#create clients and display them
class CreateClientsList(generics.ListCreateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer

#retrieve, update or delete clients by id
class RetrieveUpdateDeleteClients(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer


from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Projects
from .serializer import ProjectsSerializer

#create clients and display them
class CreateProjectsList(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

    




    