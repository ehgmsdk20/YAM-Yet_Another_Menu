from django.shortcuts import render

# Create your views here.
def searchaddr(request, input_id):
    return render(request, 'kakaomap/searchaddr.html', {'input_id': input_id})