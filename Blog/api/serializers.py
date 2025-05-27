from rest_framework import serializers

from blog_app.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post #Pointing to the Model
        fields = ["title", "summary", "content", "author"]
