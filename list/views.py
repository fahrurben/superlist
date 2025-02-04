from django.shortcuts import render
from rest_framework import viewsets

from .models import List, Item
from .serializers import ListSerializer, ItemSerializer
from .permissions import OwnerAwarePermission

class ListView(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [OwnerAwarePermission]

    def get_queryset(self):
        current_user = self.request.user
        return List.objects.filter(owner=current_user).all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

class ItemView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [OwnerAwarePermission]