
from django.urls import path
from myapp.views import *
urlpatterns = [
    path('',show.as_view(),name="showdata"),
    path("del/<int:pk>",Del.as_view(), name='delete'),
]
