from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def ourVisionView(request):
    return render(request, 'our_vision.html')
