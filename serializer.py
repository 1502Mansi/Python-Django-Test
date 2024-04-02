from rest_framework import serializers
from .models import Users
from django.utils import timezone

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('user_id', 'user_name')


from rest_framework import serializers
from .models import Clients
from django.utils import timezone

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ('client_id', 'client_name', 'created_at', 'created_by', 'updated_at')
        rof = ('created_at',  'created_by', 'updated_at')

    created_at = serializers.DateTimeField(read_only=True)


    from rest_framework import serializers
from .models import Projects
from django.utils import timezone

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('project_id', 'project_name', 'user_id', 'client_name', 'created_at', 'created_by')



    
    
        

    