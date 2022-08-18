from django.shortcuts import render

# Create your views here.
def ella(request):
    return render(request, 'JustJava.html', {})