from projects.models import Project
from rest_framework import	viewsets , permissions
from projects.serializers import ProjectSerializers

#configuracion de la api permisos
class ProjectViewSet(viewsets.ModelViewSet):
    queryset=Project.objects.all()#todo lo que contiene el objeto
    permission_classes=[permissions.AllowAny] #permite que cualquier aplicacion puede consumir la api mas adelante se tendria que cambiar AllowAny
    serializer_class=ProjectSerializers