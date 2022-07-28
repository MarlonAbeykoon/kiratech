from rest_framework import serializers

from inventory.models import Inventory, Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier

        fields = ('id', 'name')


class InventorySerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer()
    class Meta:
        model = Inventory

        fields = ('id', 'name', 'description', 'note', 'stock', 'availability', 'supplier')
