from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from app1.models import Contact
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from app1.models import Concert
from app1.forms import BookingForm
from django.core.mail import send_mail

# Create your views here.

@login_required(login_url='login')
def Homepage(request):
    return render(request, 'home.html')


def Signuppage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password1')
        contact=request.POST.get('password2')
        my_user=User.objects.create_user(username,email,password)
        my_user.save()
        return redirect('login')
      


    return render(request, 'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render(request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def about(request):
    return render(request, 'about.html')

    


def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")

        contact=Contact(name=name, email=email, phone=phone, content=content)
        contact.save()
    return render(request, 'contact.html')
    
   



def upcoming(request):
    return render(request, 'upcoming.html')

def concert_detail(request, concert_id):
    concert = get_object_or_404(Concert, pk=concert_id)
    return render(request, 'concert_detail.html', {'concert': concert})

from django.shortcuts import render, get_object_or_404
from .models import Booking
from .forms import BookingForm
from django.core.mail import send_mail


def book_now(request, concert_id):
    if request.method == 'POST':
        concert = get_object_or_404(Concert, pk=concert_id)
        
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.concert = concert
            booking.save()

            return render(request, 'thank_you.html')  # Create a thank_you.html template
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})
