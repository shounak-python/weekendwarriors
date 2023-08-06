from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Foot(models.Model):
    foot = models.CharField(
        max_length=10,
        blank=False,
        null=False,
        help_text="Preferred Foot",
    )
    def __str__(self):
        return self.foot
    class Meta:
        verbose_name_plural = "Preferred Foot"


class Proficiency(models.Model):
    pro_level = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        help_text="Beginner, Intermediate or Expert",
    )
    def __str__(self):
        return self.pro_level
    class Meta:
        verbose_name_plural = "Proficiency Level"


class FieldPosition(models.Model):
    position = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        help_text="Field Position"
    )
    def __str__(self):
        return self.position
    class Meta:
        verbose_name_plural = "Field Position"


class Member(models.Model):
    first_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="First Name"
    )
    last_name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text="Last Name"
    )
    
    image = models.ImageField(upload_to='upload/')
    
    about = models.CharField(
        max_length=500,
        blank=False,
        null=False,
        help_text="Short information about the player"
    )
    number = models.SmallIntegerField(
        blank=False,
        null=False,
        help_text="Squad Number"
    )
    preferred_foot = models.ForeignKey(Foot,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text="Preferred Foot",
        related_name = "preferred_foot"
    )
    preferred_field_position = models.ForeignKey(FieldPosition,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text="Preferred field position",
        related_name = "preferred_field_position"
    )
    secondary_field_position = models.ForeignKey(FieldPosition,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text="Secondary field position",
        related_name = "secondary_field_position"
    )
    football_proficiency = models.ForeignKey(Proficiency,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text="Football Skill Level",
        related_name = "football_proficiency"
    )
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta():
        verbose_name_plural = "Weekend Warriors Member List"