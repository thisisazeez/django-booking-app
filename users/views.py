from users.models import CustomUsers
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
import secrets


# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'
    

def SignUpView(request):
    form =  CustomUserCreationForm()
    if request.method == 'POST':
        form =  CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect ('login')
        
    else:
            form = CustomUserCreationForm()
            
    return render(request, 'registration/signup.html', {'form' : form})

