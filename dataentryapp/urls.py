from django.urls import path
#now import the views.py file into this code

from . import views
from .views import AddCitizenDataView, CreateUpdateCitizenDataView, DeleteCitizenDataView, CitizenList, CitizenDetail

urlpatterns = [
    #path('', views.index),
    path("search", views.home_view, name="search"),
    path('citizens/', CitizenList.as_view(), name='citizens'),
    path('citizen-details/<slug>', CitizenDetail.as_view(), name='citizen_detail'),
    path('add-data', AddCitizenDataView.as_view(), name='add_data'),
    path('update-data/<pk>', CreateUpdateCitizenDataView.as_view(), name='update_data'),
    path('delete-data/<pk>', DeleteCitizenDataView.as_view(), name='delete_data'),
]
