from django.db import models

class Project(models.Model):
    tittle=models.CharField(max_length=200)
    description=models.TextField()
    technology=models.CharField(max_length=200)
    create_at=models.DateField(auto_now_add=True)