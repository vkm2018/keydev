from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from apps.account.models import User


# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.text


class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings',  verbose_name='Владелец рейтинга')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings', verbose_name='Пост')
    rating = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)
    def __str__(self):
        return f'{self.post} {self.rating}'


class Comment(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post} {self.text}'