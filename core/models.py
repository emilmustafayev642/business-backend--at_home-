from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon = models.ImageField(upload_to='icons/')


    def __str__(self):
        return self.title

    
class Promo_video(models.Model):
    description = models.TextField()
    video = models.TextField()

    def __str__(self):
        return self.description[:50] 
    

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='portfloios/')
    category = models.ManyToManyField('Category',related_name='portfolios')

    def __str__(self):
        return self.title
    

class Pricing(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.CharField(max_length=100)
    description = models.TextField()
    bio_1 = models.CharField(max_length=200)
    bio_2 = models.CharField(max_length=200)
    bio_3 = models.CharField(max_length=200)
    bio_4 = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Team_Member(models.Model):
    image = models.ImageField(upload_to='team_member/')
    full_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.full_name

class Blog(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='Blog/')
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Client(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='clients/')

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.full_name
    
class Review(models.Model):
    comment = models.TextField()
    full_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    image = models.ImageField(upload_to='reviews/')

    def __str__(self):
        return self.full_name


    
