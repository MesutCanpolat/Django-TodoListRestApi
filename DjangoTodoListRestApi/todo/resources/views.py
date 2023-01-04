import random

from rest_framework import viewsets
from rest_framework.response import Response

from todo.models import Todo
from todo.resources.serializers import TodoSerializer
from rest_framework.decorators import action


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = []

    @action(["GET"], detail=False)
    def random(self, request):
        todo_count = Todo.objects.count()
        if not todo_count:
            return Response({"detail": "Not found."})
        random_todo = Todo.objects.all()[random.randint(0, todo_count - 1)]
        serializer = self.get_serializer(random_todo)
        return Response(serializer.data)
