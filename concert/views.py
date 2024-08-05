from django.shortcuts import render

def home(request):
    return render(request,'signup.html')
def LoginPage(request):
    return render(request,'login.html')
