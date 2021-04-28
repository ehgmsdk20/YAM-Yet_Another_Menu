from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def result(request, rest_list):
    rest_list=rest_list.rstrip(',').split(',')
    return render(request, 'crawling/result.html', {'rest_list': rest_list})