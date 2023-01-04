from django.urls import path, include
from rest_framework import routers

from todo.resources.views import TodoViewSet

router = routers.DefaultRouter()
router.register('todo', TodoViewSet)

urlpatterns = [
    path('v1/', include(router.urls))
]