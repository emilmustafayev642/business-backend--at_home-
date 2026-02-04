from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.

from .models import Service, Promo_video, Portfolio, Pricing, Team_Member, Blog, Category, Client, Contact, Review 
admin.site.register ({Service, Promo_video, Portfolio, Pricing, Team_Member, Blog, Category, Client, Contact, Review})
 
admin.site.unregister(Group)




