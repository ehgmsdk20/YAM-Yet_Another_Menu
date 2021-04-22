from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import forms as myforms
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile

# Create your views here.

class CustomLogoutView(LoginRequiredMixin, auth_views.LogoutView):
    template_name = 'accounts/logout.html'

def register(request):
    user_form = myforms.UserForm(request.POST or None)
    profile_form = myforms.ProfileForm(request.POST or None)
    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            return redirect('accounts:login')

    return render(request, 'accounts/register.html', {'form': user_form})

@login_required
def unregister(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('accounts:register')
    return render(request, 'accounts/unregister.html')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def editprofile(request):
    
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        if(profile):
            profile_form = myforms.ProfileForm(request.POST, instance=profile)
            if profile_form.is_valid():
                print(profile_form.cleaned_data.items())
                print("1")
                not_empty_data = [ k for k,v in profile_form.cleaned_data.items() if v!='' and v!=[] ]
                profile = profile_form.save(commit=False)
                profile.save(update_fields=not_empty_data)

        else:
            profile_form = myforms.ProfileForm(request.POST)
            if profile_form.is_valid():
                profile = profile_form.save(commit=False)
                profile.user = request.user
                profile.save()

        return redirect('accounts:profile')
    else:
        profile_form = myforms.ProfileForm()

    return render(request, 'accounts/editprofile.html', {'form': profile_form})