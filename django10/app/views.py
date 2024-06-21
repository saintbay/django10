from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse

def home(request: HttpRequest) -> HttpResponse:
    squares = [x**2 for x in range(10)]
    return JsonResponse({'squares': squares})
