from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm
from django.contrib.auth import login, logout

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # Redirect to some page after successful login
            return redirect('dashboard')  # Replace 'dashboard' with your desired URL name
    else:
        form = AuthenticationForm()
    return render(request, 'index.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to some page after successful signup
            return redirect('dashboard')  # Replace 'dashboard' with your desired URL name
    else:
        form = UserCreationForm()
    return render(request, 'index.html', {'form': form})

def forgot_password_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to some page after successfully sending reset email
            return redirect('login')  # Redirect to login page after password reset
    else:
        form = PasswordResetForm()
    return render(request, 'index.html', {'form': form})
