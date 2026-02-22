from django.db import models
from interests import models as interest_models
from django.db.models import Count

ICON_CHOICES = [
    ("fas fa-walking", "Randonnée"),
    ("fas fa-shopping-bag", "Shopping"),
    ("fas fa-utensils", "Camping"),
    ("fas fa-theater-masks", "Cyclisme"),
    ("fas fa-camera", "Football"),
    ("fas fa-horse", "Équitation"),
    ("fas fa-spa", "Spa / Bien-être"),
    ("fas fa-paint-brus", "Peinture"),
]

class Activity(models.Model):
    name = models.CharField(max_length=100, unique=True) 
    icon =models.CharField(max_length=120, choices=ICON_CHOICES,null= True, blank=True) # e.g., Randonnée, Plongée, Visite culturelle

    def __str__(self):
        return self.name


class SiteTouristique(models.Model):
    SITE_TYPE_CHOICES = (
        ('Bien_être_Spa','Bien-être & Spa'),
        ('Sports_Aventure','Sports & Aventure'),
        ('Plage', 'Plage'),
        ('Gastronomie', 'Gastronomie'),
        ('ville', 'ville'),
        ('Montagne', 'Montagne'),
        ('nature', 'nature'),
        ('history', 'history'),
    )

    name = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=50, choices=SITE_TYPE_CHOICES)
    Tarif_d_entrée= models.CharField(max_length=50, null=True, blank=True)
    Horaires =models.CharField(max_length=50, null=True, blank=True)
    site_web = models.CharField( max_length=100, null=True,blank=True)
    activities = models.ManyToManyField(Activity, blank=True)  # many activities per site
    similar_sites = models.ManyToManyField('self', blank=True)  # many similar sites
    Adresse = models.CharField(max_length=150, null=True,blank=True)
    image = models.FileField(upload_to="images", null=True,blank=True)
    contact= models.CharField(max_length=50, blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def average_rating(self):
        reviews = self.site_reviews.all()
        if reviews.exists():
            return round(sum(r.rating for r in reviews) / reviews.count(), 2)
        return 0

    def __str__(self):
        return self.name
