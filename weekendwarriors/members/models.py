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


class Club(models.Model):
    club = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        help_text="Favorite Club / Team",
    )

    def __str__(self):
        return self.club

    class Meta:
        verbose_name_plural = "Club"


class Player(models.Model):
    player = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        help_text="Favorite Football Player",
    )

    def __str__(self):
        return self.player

    class Meta:
        verbose_name_plural = "Player"


class FieldPosition(models.Model):
    position = models.CharField(
        max_length=20, blank=False, null=False, help_text="Field Position"
    )

    def __str__(self):
        return self.position

    class Meta:
        verbose_name_plural = "Field Position"


class Member(models.Model):
    first_name = models.CharField(
        max_length=100, blank=True, null=True, help_text="First Name"
    )
    last_name = models.CharField(
        max_length=100, blank=False, null=False, help_text="Last Name"
    )

    image = models.ImageField(upload_to="upload/")

    number = models.SmallIntegerField(blank=False, null=False, help_text="Squad Number")

    favorite_club = models.ForeignKey(
        Club,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text="Favorite Club",
        related_name="favorite_club",
    )

    favorite_player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text="Favorite Player",
        related_name="favorite_player",
    )

    preferred_foot = models.ForeignKey(
        Foot,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text="Preferred Foot",
        related_name="preferred_foot",
    )
    preferred_field_position = models.ForeignKey(
        FieldPosition,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text="Preferred field position",
        related_name="preferred_field_position",
    )
    secondary_field_position = models.ForeignKey(
        FieldPosition,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text="Secondary field position",
        related_name="secondary_field_position",
    )
    football_proficiency = models.ForeignKey(
        Proficiency,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text="Football Skill Level",
        related_name="football_proficiency",
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "Weekend Warriors Member List"


class Attendance(models.Model):
    date = models.DateField(unique=True)
    
    Nikhil_Kadukar = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Rajesh_Sharma = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Omkar_Panda = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Vinod_Hiwale = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Niraj_Gadhe = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Ritesh_Chambhare = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Jayant_Wani = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Neelang_Chaturvedi = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Durgesh_Patil = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Shanmukha_Vardhan = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Rahul_Dhokale = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Amod_Narhari = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Kunal_Aswale = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Sameer_Shewale = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Vaibhav_Sonar = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Prem_Jadhav = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Chirag = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Dilip_Mahajan = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Vijay_Pal = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Shounak_Deshpande = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Adwait_Sarnobat = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Umesh = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Ankit = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Satheesh = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Varun = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Prasad = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Vinit = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Sahil = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Arun = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Souvik = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Tuahar = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Sujit = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Shreekant = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name_plural = "Weekly Attendance"


class Balance(models.Model):
    date = models.DateField(unique=True)
    
    Nikhil_Kadukar = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Rajesh_Sharma = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Omkar_Panda = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Vinod_Hiwale = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Niraj_Gadhe = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Ritesh_Chambhare = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Jayant_Wani = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Neelang_Chaturvedi = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Durgesh_Patil = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Shanmukha_Vardhan = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Rahul_Dhokale = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Amod_Narhari = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Kunal_Aswale = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Sameer_Shewale = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Vaibhav_Sonar = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Prem_Jadhav = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Chirag = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Dilip_Mahajan = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Vijay_Pal = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Shounak_Deshpande = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Adwait_Sarnobat = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Umesh = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Ankit = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Satheesh = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Varun = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Prasad = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Vinit = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Sahil = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Arun = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Souvik = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Tuahar = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Sujit = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")
    Shreekant = models.SmallIntegerField(blank=False, null=False, help_text="Contribution")

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name_plural = "Weekly Balance"