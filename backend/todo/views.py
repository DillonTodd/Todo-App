from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer

# Create your views here.
@api_view(['GET'])
def todo_list(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def todo(request, id):
    todo = Todo.objects.get(id=id)
    serializer = TodoSerializer(todo)

    return Response(serializer.data)
