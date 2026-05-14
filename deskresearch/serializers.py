from rest_framework import serializers
from .models import Post, Record

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields=(
            'id','post','username','record_text','created_at'
        )

class PostSerializer(serializers.ModelSerializer):
    records = RecordSerializer(many=True,read_only=True)
    class Meta:
        model = Post
        fields = (
            'id','title','date','photo','body','rental','records'
        )