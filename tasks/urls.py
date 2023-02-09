from rest_framework import routers
from .views import CategoryViewSet, TaskViewSet

routers = routers.DefaultRouter()
routers.register(r'api/categories', CategoryViewSet, 'categories')
routers.register(r'api/tasks', TaskViewSet, 'tasks')

urlpatterns = routers.urls
