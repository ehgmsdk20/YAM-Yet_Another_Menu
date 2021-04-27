from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from . import forms as myforms

# Create your views here.
def index(request):
    return render(request, 'lunchmenu/index.html')

@login_required
def information(request):
    profile = Profile.get_or_none(Profile,user=request.user)
    if(profile):
    
        if request.method == 'POST':
            loc_form = myforms.LocChooseForm(request.POST, profile = profile)
            if loc_form.is_valid():

                loc = loc_form.cleaned_data['current_location'].lstrip('[').rstrip(']').split(',')

            return render(request, 'lunchmenu/result.html', {'lat': loc[0],
                                                            'lng': loc[1],
                                                            'radius': loc_form.cleaned_data['radius']})
    
    loc_form = myforms.LocChooseForm(profile = profile)

    return render(request, 'lunchmenu/information.html', {'form': loc_form})
    