from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def register(request):
    user_form = UserForm(request.POST or None)
    if request.method == 'POST':

        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            registered = True
            return redirect('accounts:login')

    return render(request, 'accounts/register.html', {'form': user_form,})

@login_required
def unregister(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('accounts:register')
    return render(request, 'accounts/unregister.html')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')