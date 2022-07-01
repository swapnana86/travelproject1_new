from django.http import HttpResponse
from django.shortcuts import render
from .models import Place

from . models import TeamMember
# Create your views here.
def home(request):
    place_pic = Place.objects.all()
    member_data = TeamMember.objects.all()

    return render(request, "index.html", {
        'result': place_pic,
        'result1': member_data
    })


"""

def addition(request):
    num1 =int( request.GET['number1'])
    num2 =int( request.GET['number2'])
    result = num1 + num2
    result1=num1*num2
    result2=num1-num2
    result3=num1/num2
    return render(request, "result.html", {'result_key': result,'result_key1':result1,'result_key2':result2,'result_key3':result3})


def about(request):
    return render(request, "about.html")


def contact(request):
    return HttpResponse("My contact details here")


def details(request):
    return render(request, "details.html")


def thanks(request):
    return render(request, "thanks.html")"""
