from django.contrib import admin
from voyageur import models
# Register your models here.

class voyageurAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name','get_interests']

    def get_interests(self, obj):
        return ", ".join([interest.name for interest in obj.interests.all()])
    
    get_interests.short_description = "Interests"


admin.site.register(models.Voyageur,voyageurAdmin)
