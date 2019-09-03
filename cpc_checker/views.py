from django.shortcuts import render, redirect, HttpResponse
import requests

def home(request):
    return render(request, 'home.html')


def test_cpc_cost(request):
    if request.POST:
        url = "https://cpc.farnell.com/duratool/d03214/18v-combi-hammer-drill-2ah-battery/dp/TL19684"
        header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"}
        page = requests.get(url, headers=header)
        print(page.content)