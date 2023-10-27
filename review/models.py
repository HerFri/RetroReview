from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from .stars import STARS
from .genres import GENRES
from .status import STATUS
from .years import YEARS
from .platforms import PLATFORMS

# Create your models here.


class Game(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    genre = models.CharField(max_length=100, choices=GENRES, blank=True)
    year = models.IntegerField(choices=YEARS, blank=True)
    platform = models.CharField(max_length=100, choices=PLATFORMS, blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
    developer = models.CharField(max_length=100, blank=True)
    description = models.TextField()

    class Meta:
        ordering = ['-year'] # or order by -created_on?

    def __str__(self):
        return self.title
    

class Review(models.Model):
    title = models.CharField(max_length=200, unique=True, blank=True) # default=Game.title? # can act as excerpt?
    slug = models.SlugField(max_length=200, unique=True, default='')
    username = models.ForeignKey(User, on_delete=models.CASCADE) #ForeignKey?
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    #review_image = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='review_image') #CloudinaryField('image', default='placeholder') # Users can upload their own screenshots?
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0) 
    likes = models.ManyToManyField(User, related_name='review_like', blank=True)
    rating = models.DecimalField(choices=STARS, max_digits=2, decimal_places=1) # ForeignKey?
    id = models.AutoField(primary_key=True, editable=False)    
    
    #class Meta:
    #    ordering = ['-likes'] # fails at migration

    def number_of_likes(self):
        return self.likes.count()
    
    def ordered_by_likes(self):
        return self.likes.order_by('-likes') # eingebaut in projekt?

    def __str__(self):
        return f"Review {self.content} by {self.username}"


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.author}"

