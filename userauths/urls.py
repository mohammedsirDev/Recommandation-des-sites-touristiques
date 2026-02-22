from django.urls import path
from userauths import views
from django.contrib.auth.views import LogoutView

app_name="userauths"
 
urlpatterns = [
    
    path("userauths/register/", views.register, name="register"),  
    path("userauths/login/", views.login_form, name="login_form"), 
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('userauths/password-change/',views.MypasswordChangeView.as_view(),name='password-change-view'),
  



]
