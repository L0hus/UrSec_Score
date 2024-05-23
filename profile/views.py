from django.shortcuts import redirect, render
from loguru import logger
from profile.forms import LoginForm
from django.contrib.auth import login


def login_page(request):
    login_form = LoginForm()
    
    if request.method == "POST":
        login_form = LoginForm(request, request.POST)
        
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('index')
        
    return render(request, "login.html", {"form": login_form})