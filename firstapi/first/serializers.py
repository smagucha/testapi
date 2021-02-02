from rest_framework import serializers
from .models import Article

# class ArticleSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     email = serializers.EmailField()
#     comment = serializers.TextField()
#
#     def create(self, validate_data):
#         return Article.objects.create(validate_data)
#
#     def update(self, instance, validate_data):
#         instance .name = validate_data.get('name', instance.name)
#         instance .email = validate_data.get('name', instance.email)
#         instance .comment = validate_data.get('name', instance.comment)
#         instance.save()
#         return instance

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields= '__all__'
