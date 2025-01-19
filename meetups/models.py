from django.db import models

# Create your models here.



class Participants(models.Model):
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Location(models.Model):
    name=models.CharField(max_length=200)
    adress=models.TextField()

    def __str__(self):
        return self.name


class Meetups(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    organizer_email=models.EmailField()
    date=models.DateField()
    description = models.TextField()
    image=models.ImageField(upload_to='images')
    location=models.ForeignKey(Location, on_delete=models.CASCADE)
    participants=models.ManyToManyField(Participants, blank=True )

    def __str__(self):
        return f'{self.title} - {self.slug}'