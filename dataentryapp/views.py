from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CitizenForm
from .models import Citizen


class LandingPageView(generic.TemplateView):
    template_name = "landing.html"

    #def dispatch(self, request, *args, **kwargs):
    #   if request.user.is_authenticated:
    #        return redirect("search")
    #    return super().dispatch(request, *args, **kwargs)

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def home_view(request):
    context ={}
 
    # create object of form
    form = CitizenForm(request.POST )
     
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
    else:
        form = CitizenForm()
    context['form']= form
    return render(request, "dataentryapp/search.html", {"form": form})

def search_result(request):
    return render(request, "dataentryapp/results.html")