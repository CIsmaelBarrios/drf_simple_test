from rest_framework import serializers
from .models import Project

class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=('id','tittle','description','technology','create_at')
        read_only_fields=('create_at',)