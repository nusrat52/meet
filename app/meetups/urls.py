from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name="meetups"),
    path('<slug:slug_success>/succes-page', views.succes_view, name="successPageName"),
    path('<slugg>', views.detail_meetup, name="meetup_slug"),

]