from django.shortcuts import render
from django.http import JsonResponse
from .utils import fetch_news

# Create your views here.

def latest_news(request):
    articles = fetch_news()
    headlines = [{"title": a[0], "description": a[1]} for a in articles]
    # headlines = [{"title": t} for t in titles]
    return JsonResponse({"headlines": headlines})