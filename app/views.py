from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.user_type == 'patient':
                return redirect('patient_dashboard')
            elif user.user_type == 'doctor':
                return redirect('doctor_dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')

@login_required
def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html')


@login_required
def login_redirect(request):
    if request.user.user_type == 'patient':
        return redirect('patient_dashboard')
    elif request.user.user_type == 'doctor':
        return redirect('doctor_dashboard')


def home(request):
    if request.user.is_authenticated:
        if request.user.user_type == 'patient':
            return redirect('patient_dashboard')
        elif request.user.user_type == 'doctor':
            return redirect('doctor_dashboard')
    return redirect('login')