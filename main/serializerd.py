from rest_framework.serializers import ModelSerializer
from .models import Book, Rating

class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if instance.rating_book.exists():
            rep['rating'] = RatingSerializer(instance.rating_book.all()[0]).data
        return rep