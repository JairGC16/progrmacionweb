from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from .forms import RegisterForm, ProfileForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        form = RegisterForm()
        profile_form = ProfileForm()
    return render(request, 'accounts/register.html', {'form': form, 'profile_form': profile_form})

def login_view(request):
    form = LoginForm(request, data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        
        # Obtén el perfil del usuario para verificar el rol
        profile = Profile.objects.get(user=user)
        
        # Redirige a item_forms si el rol es admin, de lo contrario a user_list
        if profile.role == 'admin':
            return redirect('home')
        else:
            return redirect('homeuser')
    
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'accounts/user_list.html', {'users': users})

@login_required
def user_update(request, id):
    user = get_object_or_404(User, id=id)
    profile = user.profile
    form = RegisterForm(request.POST or None, instance=user)
    profile_form = ProfileForm(request.POST or None, instance=profile)
    if form.is_valid() and profile_form.is_valid():
        form.save()
        profile_form.save()
        return redirect('user_list')
    return render(request, 'accounts/user_form.html', {'form': form, 'profile_form': profile_form})

@login_required
def user_delete(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'accounts/user_confirm_delete.html', {'user': user})
