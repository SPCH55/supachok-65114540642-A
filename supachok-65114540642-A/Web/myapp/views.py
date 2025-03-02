from django.shortcuts import render
from django.views.generic import ListView , DeleteView
from .models import course
# Create your views here.
class show(ListView):
    model = course
    context_object_name = "course"
    template_name = "show.html"
    field = ["course_id","course_name"]

class Del(DeleteView):
    model = course
    template_name = "delete.html"
    field = ["course_id","course_name"]
    