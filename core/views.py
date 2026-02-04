from django.shortcuts import render
from core.models import *
def home(request):
    services = Service.objects.all()
    promo_videos = Promo_video.objects.all()
    pricing = Pricing.objects.all()
    all_portfolios = Portfolio.objects.order_by('-id')
    branding_portfolios = Portfolio.objects.filter(category__name='BRANDING')
    marketing_portfolios = Portfolio.objects.filter(category__name='MARKETING')
    planning_portfolios = Portfolio.objects.filter(category__name='PLANNING')
    reseach_portfolios = Portfolio.objects.filter(category__name='RESEARCH')
    clients = Client.objects.all()
    category = Category.objects.all()
    blogs = Blog.objects.all()
    team_member = Team_Member.objects.all()
    
    context = {
        'services': services,
        'promo_videos': promo_videos,
        'pricings' : pricing,
        'all_portfolios' : all_portfolios,
        'clients' : clients,
        'category' : category,
        'blogs' : blogs,
        'team_members' : team_member,
        'branding_portfolios' : branding_portfolios,
        'all_portfolios' : all_portfolios,
        'branding_portfolios' : branding_portfolios,
        'marketing_portfolios' : marketing_portfolios,
        'planning_portfolios' : planning_portfolios,
        'reseach_portfolios' : reseach_portfolios,

    }
    return render(request, 'index.html', context)
