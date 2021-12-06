from django.db import models
from django.shortcuts import render
from django.views.generic import ListView,DetailView

from .models import Snacks


class SnackListView(ListView):
    template_name = "home.html"
    model = Snacks


class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snacks