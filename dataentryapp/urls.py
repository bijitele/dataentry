from django.urls import path
#now import the views.py file into this code

from . import views
from .views import AddCitizenDataView, CreateUpdateCitizenDataView

urlpatterns = [
    #path('', views.index),
    path("search", views.home_view, name="search"),
    path("thank-you", views.search_result, name="thank_you"),
    path("add-data", CreateUpdateCitizenDataView.as_view(), name="add_data"),
]
