from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Question, ip_mamont

from django.shortcuts import render
from .forms import QuestionForm, IP


def home(request):
    x_forward = request.META.get("HTTP_X_FORWADED_FOR")
    if x_forward:
        cip = x_forward.split(",")[0]
    else:
        cip = request.META.get("REMOTE_ADDR")

    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():  
            data = form.cleaned_data
            ip_mamont.objects.create(ip=cip)
            form.save()
    else:
        form = QuestionForm()
        
    return render(request, 'poll/home.html', {'form': form})
    print(ip_mamont.ip)

def garanties(request):
    return render(request, 'poll/garanties.html')

def about(request):
    return render(request, 'poll/about.html')