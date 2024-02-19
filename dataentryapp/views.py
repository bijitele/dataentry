from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import CitizenForm
from .models import Citizen
from .forms import SignUpForm, UserForm, ProfileForm

class LandingPageView(generic.TemplateView):
    template_name = "landing.html"

    #def dispatch(self, request, *args, **kwargs):
    #   if request.user.is_authenticated:
    #        return redirect("search")
    #    return super().dispatch(request, *args, **kwargs)


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('signup')
    template_name = "registration/signup.html"
    success_message = "User %(username)s was created successfully"
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)


#class LoginView(generic.CreateView):


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