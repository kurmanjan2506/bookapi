from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='image/')

# user = request.user
class Rating(models.Model):
    RATING = (
        ('1', 'очень плохо'),
        ('2', 'плохо'),
        ('3', 'пойдет'),
        ('4', 'намальна'),
        ('5', 'ништяк')
    )
    rating = models.CharField(max_length=30, choices=RATING)
    book = models.ForeignKey(Book, related_name='rating_book', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='rating_user', on_delete=models.CASCADE)