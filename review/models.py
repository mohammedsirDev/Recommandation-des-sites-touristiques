from django.db import models
from sites import models as sites_models
from userauths import models as  user_models

RATING_CHOICES = [
        (1, '1 ⭐'),
        (2, '2 ⭐⭐'),
        (3, '3 ⭐⭐⭐'),
        (4, '4 ⭐⭐⭐⭐'),
        (5, '5 ⭐⭐⭐⭐⭐'),
    ]

class Review(models.Model):
    site = models.ForeignKey(sites_models.SiteTouristique, on_delete=models.CASCADE, related_name='site_reviews')
    user = models.ForeignKey(user_models.User, null=True, blank=True, on_delete=models.SET_NULL, related_name='user_reviews')
    user_name = models.CharField(max_length=100, blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES) # 1-5
    title = models.CharField(max_length=200)
    comment = models.TextField(null=True, blank=True)
    visit_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return f"{self.user.username if self.user else self.user_name or 'Anonyme'} - {self.site.name}"
