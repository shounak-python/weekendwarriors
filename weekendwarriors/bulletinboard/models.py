from django.db import models

# Create your models here.

class Bulletin(models.Model):
    title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text="Title of Bulletin",
    )

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    
    subtitle = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        help_text="Subtitle of Bulletin",
    )

    content = models.TextField()

    image = models.ImageField(upload_to="upload/bulletin/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Bulletin Board"