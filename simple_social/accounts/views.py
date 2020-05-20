from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

from . import models
# Create your views here.


class SignUp(CreateView):
    model = models.User
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
