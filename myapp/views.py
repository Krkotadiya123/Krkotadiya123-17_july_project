from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout
from django.core.mail import send_mail
import random
from mybatchproject import settings

# Create your views here.
def home(request):
    data=request.session.get('cuser')
    return render(request,'home.html',{'data':data})

def login(request):
    if request.method=='POST':
        us=request.POST['email']
        pas=request.POST['password']
        user=top_tach.objects.filter(email=us,password=pas)
        
        if user:
            request.session['cuser']=us
            return redirect('/')
        else:
            print('error')

    return render(request,'login.html')

def signup(request):
    msg=" "
    global otp
    global user
    if request.method=='POST':
        unm=request.POST['email']
        user=top_tach_form(request.POST)
       
        exist=top_tach.objects.filter(email=unm)

        if exist:
            msg="Account already"
            return render(request,'signup.html',{'msg':msg})

        if user.is_valid():
            user.save()
            print("signup succ.")

            #sand otp

            
            otp=random.randint(1111,9999)
            sub="Your One Time Password"
            msg=f"Hello User!\n\nThanks for registration with us!\n\nYour one time password is {otp}.\n\nThanks & Regards!\nNotesApp Tech - Rajkot  \n 9106903090 \n kevalkotadiya94@gmail.com"
            from_ID=settings.EMAIL_HOST_USER
            to_ID=unm
            send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=[to_ID])

            return redirect('otp')
        else:
            print(user.errors)
    return render(request,'signup.html',{'msg':msg})

def userlogout(request):
    logout(request)
    return redirect('login')


def profile(request):
    data=request.session.get('cuser')
    f_data=top_tach.objects.all().filter(email=data)

    return render(request,'profile.html',{'data':data,'f_data':f_data},)

def contect(request):
    data=request.session.get('cuser')
    if request.method == 'POST':
        new_req =contact_form(request.POST)
        if new_req.is_valid():
            new_req.save()
            print('your contact from is succ...')

            #email sending
            sub="Your One Time Password"
            msg=f"Hello !\n\nThanks for registration with us!\n\nThanks & Regards!\nNotesApp Tech - Rajkot  \n 9106903090 \n kevalkotadiya94@gmail.com"
            from_ID=settings.EMAIL_HOST_USER
            to_ID=request.POST['mail']
            send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=[to_ID])


        else:
            print(new_req.errors)
    return render(request,'contect.html',{'data':data})

def about(request):
    data=request.session.get('cuser')
    return render(request,'about.html')

def notes(request):
    
    data = request.session.get('cuser') 
    if request.method == 'POST':
        new_req = notesFrom(request.POST,request.FILES)
        if new_req.is_valid():
            new_req.save()
        else:
            print(new_req.errors)
    return render(request,'notes.html',{'data':data})




def otp(request):
    msg=""
    if request.method=='POST':
        if request.POST['otp']==str(otp):
            user.save()
            print("Verification done!")
            return redirect('login')
        else:
            print("Error!Invalid OTP")
            msg="Error!Invalid OTP"
    return render(request,'otp.html',{'msg':msg})
   
def update_profile(request):
    data=request.session.get('cuser')
    cu=top_tach.objects.get(email=data)

    if request.method=='POST':
        update_re=updateform(request.POST,instance=cu)
        if update_re.is_valid():
            update_re.save()
            print("Your profile has been updated!")
            
            return redirect('/')
        else:
            print(update_re.errors)
    return render(request,'update_profile.html',{'data':data,'cu':cu})

def service(request):
    data=request.session.get('cuser')
    return render(request,'service.html',{'data':data})