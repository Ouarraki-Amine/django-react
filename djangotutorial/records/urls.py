from django.urls import path

from . import views

urlpatterns = [
    path("", views.records_list, name="records_list"),  
    path("<int:id>", views.record_detail, name="record_detail"),
]