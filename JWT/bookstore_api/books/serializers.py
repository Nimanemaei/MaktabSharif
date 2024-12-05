from rest_framework import serializers
from .models import Author, Book, User

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.name')
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'slug', 'author_name', 'published_date', 'price']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be positive.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'biography', 'books']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'is_active']
