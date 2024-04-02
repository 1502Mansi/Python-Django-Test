from django.db import models

#create your models here

#user - id, user_name

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length = 255)


from django.db import models

#client - id, client_name, created_at, created_by

class Clients(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    created_by = models.CharField(max_length=255, default='Rohit')
    updated_at = models.DateTimeField(auto_now=True)


from django.db import models

#create your models here

#project - id, project_name

class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length = 255)
    




    
