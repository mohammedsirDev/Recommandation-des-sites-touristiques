from django.contrib import admin
from review import models as review_models
# Register your models here.
admin.site.register(review_models.Review)