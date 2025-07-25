from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required

def redirect_dashboard(user):
    if user.user_type == 'client':
        return redirect('client_dashboard')
    elif user.user_type == 'provider':
        return redirect('provider_dashboard')
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect_dashboard(user)
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect_dashboard(user)
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'home.html')

@login_required
def client_dashboard(request):
    return render(request, 'accounts/client_dashboard_search.html')

@login_required
def client_call_history(request):
    return render(request, 'accounts/client_dashboard_history.html')

@login_required
def client_payment(request):
    return render(request, 'accounts/client_dashboard_payment.html')

def provider_dashboard(request):
    return render(request, 'accounts/provider_dashboard.html')
