from django.shortcuts import render,get_object_or_404,redirect
from sites import models as sites_models
# Create your views here.
from django.db.models import Count
from review.forms import ReviewForm 
from django.contrib.auth.decorators import login_required
from voyageur.models import Voyageur





def index(request):
    sites = sites_models.SiteTouristique.objects.all()
    sites_by_type = (
        sites_models.SiteTouristique.objects
        .values('type')
        .annotate(total=Count('id'))
        .order_by('-total'))
    sites_count = {item['type']: item['total'] for item in sites_by_type}
    context={
        "sites":sites,
        "sites_count": sites_count
    }
    return render(request,"sites/index.html",context)

def sites_detail(request,sites_id):
    site = sites_models.SiteTouristique.objects.get(id=sites_id)
    form=ReviewForm()
    reviews = site.site_reviews.all()
    similar_sites = site.similar_sites.all()
    context={
        "site":site,
        "form":form,
        "reviews":reviews,
        "similar_sites":similar_sites
        
      
       
    }
    return render(request,"sites/site_detail.html",context)

def add_review(request,sites_id):
    site = get_object_or_404(sites_models.SiteTouristique, id=sites_id)
    if request.method=="POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.site = site
            review.save()
      
    else:
        form = ReviewForm() 
          
    return redirect('sites:sites_detail', sites_id=site.id)
     
def site_par_type(request,sites_type):
    sites = sites_models.SiteTouristique.objects.filter(type=sites_type)
    sites_count = sites.count()
   
    
    context={
        "sites":sites,
        "sites_count": sites_count
        
    }
    return render(request, "sites/site_par_type.html", context)

from django.db.models import Q

def afficher_sites(request):

    query = request.GET.get("q", "")
    site_type = request.GET.get("type", "")

    sites = sites_models.SiteTouristique.objects.all()

    # Search system
    if query:
        sites = sites.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(Adresse__icontains=query)
        )

    # Type filter
    if site_type:
        sites = sites.filter(type=site_type)

    # Dropdown choices
    type_choices = sites_models.SiteTouristique.objects\
        .exclude(type="")\
        .values_list('type', flat=True)\
        .distinct()

    return render(request, "sites/sites_pages.html", {
        "sites": sites,
        "type_choices": type_choices,
        "query": query
    })

def recommendations(request):
     sites = sites_models.SiteTouristique.objects.all()
     context={
         "sites":sites
     }
     return render(request,"sites/recommendations.html",context)

@login_required(login_url='/userauths/login/')
def toggle_favorite(request, site_id):
    
    site = get_object_or_404(sites_models.SiteTouristique, id=site_id)

    voyageur = Voyageur.objects.get(user=request.user)

    if site in voyageur.favorite_sites.all():
        voyageur.favorite_sites.remove(site)
    else:
        voyageur.favorite_sites.add(site)

    return redirect(request.META.get('HTTP_REFERER', '/'))
@login_required(login_url='/userauths/login/')
def favorites(request):
    voyageur = Voyageur.objects.get(user=request.user)
    favorites = voyageur.favorite_sites.all()

    return render(request, "sites/favorite.html", {
        "favorites": favorites
    })
