from django.urls import path
from .views import CreateUsersList, RetrieveUpdateDeleteUsers

urlpatterns = [
    path('users', CreateUsersList.as_view(), name='Create-Users-List'),
    path('users/<int:pk>/', RetrieveUpdateDeleteUsers.as_view(), name='User-Details'),
]


from django.urls import path
from .views import CreateClientsList, RetrieveUpdateDeleteClients

urlpatterns = [
    path('clients', CreateClientsList.as_view(), name='Create-Clients-List'),
    path('clients/<int:pk>/', RetrieveUpdateDeleteClients.as_view(), name='Client-Details'),
]


from django.urls import path
from .views import CreateProjectsList, RetrieveUpdateDeleteProjects

urlpatterns = [
    path('projects', CreateProjectsList.as_view(), name='Create-Projects-List'),
    path('projects/<int:pk>/', RetrieveUpdateDeleteProjects.as_view(), name='Project-Details'),
]