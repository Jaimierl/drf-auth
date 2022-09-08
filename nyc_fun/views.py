from rest_framework import generics
from .serializer import ThingSerializer
from .models import ToDo
from .permissions import IsOwnerOrReadOnly


class ToDoList(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ThingSerializer


class ToDoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = ToDo.objects.all()
    serializer_class = ThingSerializer
