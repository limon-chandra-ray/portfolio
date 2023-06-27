from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')


def skill(request):
    return render(request,'skill.html')

def contactus(request):
    return render(request,'contactus.html')

def study(request):
    return render(request,'study.html')

def exprience(request):
    return render(request,'exprience.html')

