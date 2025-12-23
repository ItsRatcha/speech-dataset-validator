from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Lang(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Audio(models.Model):
    id = models.AutoField(primary_key=True)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    audio = models.URLField()
    transcript = models.TextField()

    def __str__(self):
        return f"Audio {self.id} - {self.lang.name}"


class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    pronounciation_score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    naturalness_score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    noise_score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    edit_transcript = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating {self.id} - User {self.uid.username}"