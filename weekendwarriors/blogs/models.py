from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings
# from taggit.managers import TaggableManager


# Create your models here.


class Blogs(models.Model):
    title = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(5, "Title must be minimum 5 characters.")],
    )
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta():
        verbose_name_plural = "Blogs"

