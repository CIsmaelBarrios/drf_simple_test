from rest_framework import routers #crea las rutas de manera automnatica
from .api import ProjectViewSet 

#crea 4 url para POST, GET, ETC
router=routers.DefaultRouter()
router.register('api/projects',ProjectViewSet,'projects')
urlpatterns=router.urls