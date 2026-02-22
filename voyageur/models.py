
# Create your models here.
from django.db import models
from userauths import models as userauth_models
from sites import models as sites_models
from interests import models as interests_models
# Create your models here.

class Voyageur(models.Model):
    user = models.OneToOneField(userauth_models.User,on_delete=models.CASCADE)
    image = models.FileField(upload_to="images", null=True,blank=True)
    full_name = models.CharField(max_length=100,blank=True, null=True)
    interests = models.ManyToManyField(interests_models.Interest, blank=True)
       # Favourite sites list
    favorite_sites = models.ManyToManyField(
        sites_models.SiteTouristique,
        blank=True,
        related_name="favorited_by"
    )
    def __str__(self):
        return self.full_name or "User"


