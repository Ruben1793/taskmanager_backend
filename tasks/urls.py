from rest_framework import routers
from .views import CategoryViewSet

routers = routers.DefaultRouter()
routers.register(r'api/categories', CategoryViewSet, 'categories')

urlpatterns = routers.urls