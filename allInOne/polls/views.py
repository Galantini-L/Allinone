from django.shortcuts import render
from django.http import HttpResponse
from random import choices

def index(request):
    return HttpResponse('Hello, this is my poll app!')


def number(request):
    ranNum = choices('123456789')
    return HttpResponse(f'this is a random number {ranNum[0]}')
