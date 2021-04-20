from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import forms as myforms
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class CustomLogoutView(LoginRequiredMixin, auth_views.LogoutView):
    template_name = 'accounts/logout.html'

def register(request):
    user_form = myforms.UserForm(request.POST or None)
    profile_form = myforms.ProfileForm(request.POST or None)
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            if profile_form.is_valid():
                profile = profile_form.save(commit=False)
                profile.user = user     #connect user with profile
                user.save()
                profile.save()
                return redirect('accounts:login')

    return render(request, 'accounts/register.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def unregister(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('accounts:register')
    return render(request, 'accounts/unregister.html')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')