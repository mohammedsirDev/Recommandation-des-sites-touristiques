from django.urls import path
from sites import views
app_name="sites"

urlpatterns = [
    path("sites/favorite/", views.favorites, name="favorites"),
    path('sites/sites_pages', views.afficher_sites, name='afficher_site'),
    path("",views.index,name="index"),
    path("sites/<sites_id>/",views.sites_detail, name="sites_detail"),
    path('sites/<sites_id>/add_review/', views.add_review, name='add_review'),
    path('sites/<sites_type>/site_par_type/', views.site_par_type, name='site_par_type'),
 
    path('sites/recommendations', views.recommendations, name='recommendations'),
    path("sites/<int:site_id>/favorites/", views.toggle_favorite, name="toggle_favorite"),
     



]
