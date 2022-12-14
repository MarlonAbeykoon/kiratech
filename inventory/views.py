import requests
from django.shortcuts import render

from rest_framework import status, viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from inventory.models import Inventory
from inventory.serializers import InventorySerializer


class InventoryListApiView(APIView):

    def get(self, request, *args, **kwargs):
        name = self.request.query_params.get('name', None)
        inventories = self.get_data(name)
        serializer = InventorySerializer(inventories, many=True)

        return Response({"inventories": serializer.data}, status=status.HTTP_200_OK)

    def get_data(self, name):
        inventories = Inventory.objects.select_related('supplier').all()
        if name:
            inventories = inventories.filter(name=name)
        return inventories

def getInventories(request):
    inventories = requests.get('http://localhost:8000/api/inventory/').json() # can be taken from a env
    return render(request, 'inventories.html', {'response': inventories['inventories']})


class TodoDetailApiView(viewsets.ModelViewSet):
    template_name = 'inventory_detail.html'
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = InventorySerializer

    def get(self, request, id, *args, **kwargs):
        queryset = self.get_data(id)
        return Response({'response': queryset}, status=status.HTTP_200_OK)

    def get_data(self, id):
        return Inventory.objects.get(id=id)