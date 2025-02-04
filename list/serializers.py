from rest_framework import serializers

from .models import List, Item

class ItemSerializer(serializers.ModelSerializer):
    list_id = serializers.IntegerField()

    class Meta:
        model = Item
        fields = '__all__'

class ListSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    items = ItemSerializer(source="item_set", many=True, read_only=True)

    class Meta:
        model = List
        fields = '__all__'

    def create(self, validated_data):
        current_user = self.context['request'].user
        list = List(**validated_data)
        list.owner = current_user
        list.save()
        return list