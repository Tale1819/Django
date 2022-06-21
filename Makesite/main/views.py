from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'main/main.html')


def proflie(request):
    return render(request, 'main/proflie.html')


def work(request):
    return render(request, 'main/work.html')


def like(request):
    return render(request, 'main/like.html')


def sns(request):
    return render(request, 'main/sns.html')
