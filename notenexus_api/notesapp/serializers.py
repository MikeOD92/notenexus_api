from rest_framework import serializers 
from .models import Node, Note 


class CreateNodeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Node
        fields = ['subject_title', 'user']

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"

class NodeSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True)
    class Meta: 
        model = Node
        fields = ['subject_title', 'notes']