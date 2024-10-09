from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Create user instance without saving
            user.set_password(form.cleaned_data['password'])  # Set the password properly
            user.save()  # Now save the user to the database
            return redirect('login')  # Redirect to the login page after successful signup
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard after successful login
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)  # Return 401 status for invalid credentials
    return render(request, 'login.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})  # Pass the user object to the template


