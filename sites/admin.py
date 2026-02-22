from django.contrib import admin
from django.utils.html import format_html
from sites import models

class SiteAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'type',
        'Tarif_d_entrée',
        'Horaires',
        'site_web',
        'display_activities',
        'display_similar_sites'
    ]
    search_fields = ['name', 'type']  # Optional: makes it easier to search
    list_filter = ['type']             # Optional: filter by site type

    def display_activities(self, obj):
        # Return activities as a comma-separated list
        return ", ".join([activity.name for activity in obj.activities.all()])
    display_activities.short_description = "Activities"

    def display_similar_sites(self, obj):
        # Return similar sites as a comma-separated list
        return ", ".join([site.name for site in obj.similar_sites.all()])
    display_similar_sites.short_description = "Similar Sites"

# Register the models

class ActivityAdmin(admin.ModelAdmin):
    list_display =["name","icon"]
admin.site.register(models.Activity,ActivityAdmin)
admin.site.register(models.SiteTouristique, SiteAdmin)
