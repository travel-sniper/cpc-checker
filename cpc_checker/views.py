from django.shortcuts import render, redirect, HttpResponse


def home(request):
    return render(request, 'home.html')


def test_cpc_cost(request):
    if request.POST:
        pass
