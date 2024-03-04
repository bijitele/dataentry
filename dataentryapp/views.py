from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
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

class CitizenDetail(DetailView):
    model = Citizen
    context_object_name = 'citizenDetail'
    pk_url_kwarg = "unique_govt_id"

class AddCitizenDataView(CreateView):
    model = Citizen
    form_class = CitizenForm
    success_url = reverse_lazy('add_data')
    template_name = "dataentryapp/create_data.html"
    success_message = "Citizen data for %(first_name) was added successfully"

class CreateUpdateCitizenDataView(UpdateView):
    model = Citizen
    form_class = CitizenForm
    success_url = reverse_lazy('add_data')
    template_name = "dataentryapp/create_data.html"
    success_message = "Citizen data for %(first_name) was added successfully"
 
    def get_object(self, queryset=None):
        print("inside get: post")
        if self.request.method == 'POST':
            print("it is posted")
            return self.model.objects.filter(first_name=self.request.POST.get('first_name'), 
                                            last_name=self.request.POST.get('last_name'), dob=self.request.POST.get('dob')).first()

class DeleteCitizenDataView(DeleteView):
    model = Citizen
    form_class = CitizenForm
    success_url = reverse_lazy('add_data')
    template_name = "dataentryapp/delete_data.html"
    success_message = "Citizen data for %(first_name) was been removed successfully"

class CitizenList(ListView):
    model = Citizen
    context_object_name = 'citizenlist'
    template_name = "dataentryapp/citizen_list.html"


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