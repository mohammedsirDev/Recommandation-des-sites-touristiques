from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from voyageur.models import Voyageur
from interests.models import Interest
from django.contrib.auth import login,authenticate
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import CustomPasswordChangeForm




def login_form(request):

    print("LOGIN VIEW EXECUTED")

    if request.method == "POST":
        print("POST REQUEST RECEIVED")

        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
      
        print(f"TRY AUTH → username={email} password={password}")

        user = authenticate(
            request,
            email=email,
            password=password
        )
        print("AUTH RESULT:", user)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return redirect("/userauths/login/")

    return render(request, "userauths/login.html")




def register(request):
    
    interests_list = Interest.objects.all() 


    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()

            full_name = f"{form.cleaned_data.get('first_name')} {form.cleaned_data.get('last_name')}"

            voyageur = Voyageur.objects.create(
                user=user,
                full_name=full_name
            )

            # Interests handling
            interest_ids = request.POST.getlist("interests")
            interests = Interest.objects.filter(id__in=interest_ids)
            voyageur.interests.set(interests)

            messages.success(request, "Votre compte a été créé avec succès !")
            login(request,user)
            return redirect("/")

    else:
        form = RegisterForm()

    return render(request, "userauths/register.html", {
        "form": form,
        "interests": interests_list
    })

class MypasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'userauths/password-change.html'
    success_url = "/"
    

from django.http import HttpResponse
from django.conf import settings





