from django.shortcuts import render,redirect
from django.contrib import messages
import bcrypt
from . models import *
# Create your views here.


def log_reg(request):
    return render(request,"log_reg.html")

def create_user(request):
    errors=Dealer.objects.dealer_validator(request.POST)
    if len(errors)> 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        password=request.POST['password']
        pw_hash=bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()

    
    the_user=Dealer.objects.create(
        first_name=request.POST['fname'],
        last_name=request.POST['lname'],
        email=request.POST['email'],
        password=pw_hash
        
    )
    
    request.session['userid']=the_user.id
    
    messages.success(request,"succssfully created a user")
    return redirect('cars')


def login(request):
    errors=Dealer.objects.login_validator(request.POST)
    user=Dealer.objects.filter(email=request.POST['email'])
    if user:
        logged_user=user[0]
        if bcrypt.checkpw(request.POST['password'].encode(),logged_user.password.encode()):
            request.session['userid']=logged_user.id
            # messages.success(request,"succssesfully register or logged in")
            cars=Car.objects.all()
          
            return redirect('cars')
    messages.error(request,"Invalid Password or Email")

    return redirect("/")

def success(request):
    user_id=request.session['userid']
    logged_user=Dealer.objects.get(id=user_id)
    
    context={
        "logged":logged_user,
        "cars":Car.objects.all(),
        "dealer":Dealer.objects.all()
    }
    return render (request,"welcome.html",context)




def logged_out(request):
    if request.session['userid']:
        del request.session['userid']

    return redirect('/')


def view(request,id):
    car=Car.objects.get(id=id)
    context={
        "car":car
    }
    return render(request,"view.html",context)


def new(request):
    user_id=request.session['userid']
    logged_user=Dealer.objects.get(id=user_id)
    context={
        "logged":logged_user,
        "cars":Car.objects.all(),
        "dealer":Dealer.objects.all()
    }
    return render(request,"post.html",context)

def post(request):
    errors2 = Car.objects.car_validator(request.POST)
    # if len(errors2)> 0:
    #     for key, value in errors2.items():
    #         messages.error(request, value)
    #     return redirect('new')
    
    if errors2:
        for error in errors2:
            messages.error(request, error)
    else:
        if request.method=="POST":
            user_id=request.session['userid']
            logged_user=Dealer.objects.get(id=user_id)
            context={
                "logged":logged_user,
                 "cars":Car.objects.all(),
                 "dealer":Dealer.objects.all
            }
            Car.objects.create(
                price=request.POST['price'],
                model=request.POST['model'],
                desc=request.POST['desc'],
                make=request.POST['make'],
                year=request.POST['year'],
                seller_con=request.POST['seller_con'],
                dealer_id_id=request.POST['dealer_id']
        )
            messages.success(request, "Show successfully created")
        return redirect('cars')


def edit(request,id):
    errors2 = Car.objects.car_validator(request.POST)
    user_id=request.session['userid']
    logged_user=Dealer.objects.get(id=user_id)
    id=user_id
    context={
        "logged":logged_user
    }
    return render(request,"edit.html",context,id=id)


def postedit(request,id):
    errors2 = Car.objects.car_validator(request.POST)
    if errors2:
        for error in errors2:
            messages.error(request, error)
        return redirect('edit',id=id)
    else:
        if request.method=="POST":
            selected=Car.objects.get(id=id)
         
            selected.price=request.POST['title']
            selected.model=request.POST['network']
            selected.year=request.POST['release']
            selected.desc=request.POST['desc']
            selected.save()
            messages.success(request, "Show successfully created")
    return redirect('cars',id=id)
    

def cancel(request):
    return redirect('cars')



def destroy(request,id): 
    selected=Car.objects.get(id=id)
    selected.delete()
    return redirect('cars',id=id)