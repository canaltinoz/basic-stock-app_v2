from django.shortcuts import render, redirect
from .forms import SignUpForm,LoginForm,AddFlavourForm,FlavourTransactionForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .models import Flavour,CustomUser,Transaction

def home(request):
    return render(request,'app/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'app/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home') 
    else:
        form = LoginForm()
    return render(request, 'app/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect("home")

def user_details(request):
    user = request.user
    return render(request, 'app/user_details.html', {'user': user})

@login_required
def flavour_transaction(request):
    if request.method == 'POST':
        form = FlavourTransactionForm(request.POST)
        if form.is_valid():
            action = form.cleaned_data['action']
            flavour = form.cleaned_data['flavour']
            quantity = form.cleaned_data['quantity']
            user_profile = CustomUser.objects.get(pk=request.user.pk)

            if action == 'decrease':
                flavour.quantity -= quantity
                if flavour.quantity<0:
                    return render(request,'app/error_flavour.html',{'error_message': 'Insufficient balance','quantity':int(flavour.quantity+quantity)})
                user_profile.balance += quantity

            elif action == 'increase':
                flavour.quantity += quantity
                user_profile.balance -= quantity
                if user_profile.balance<0:
                     return render(request, 'app/error.html', {'error_message': 'Insufficient balance','balance':int(user_profile.balance+quantity)})

            flavour.save()
            user_profile.save()
            return redirect('list_flavour')
    else:
        form = FlavourTransactionForm()
    user_profile = CustomUser.objects.get(pk=request.user.pk)
    return render(request, 'app/update.html', {'form': form,'balance':user_profile.balance})

@login_required
def profile_view(request):
    user_profile = CustomUser.objects.get(pk=request.user.pk)
    transactions = Transaction.objects.filter(pk=request.user.pk)
    return render(request, 'profile.html', {'user_profile': user_profile, 'transactions': transactions})

@login_required
def add_flavour(request):
    if request.method == 'POST':
        form = AddFlavourForm(request.POST)
        if form.is_valid():
            flavour = form.save(commit=False)
            user_profile = CustomUser.objects.get(pk=request.user.pk)
            total_cost = flavour.quantity  

            if total_cost > user_profile.balance:
                return render(request, 'app/error.html', {'error_message': 'Insufficient balance','balance':user_profile.balance})

            flavour.save()
            user_profile.balance -= total_cost
            user_profile.save()
            return redirect('list_flavour')
    else:
        form = AddFlavourForm()
    return render(request, 'app/upload.html', {'form': form})

@login_required
def list_flavour(request):
    flavour = Flavour.objects.all()
    return render(request, 'app/list.html', {'flavour': flavour})

@login_required
def delete(request,id):
    flavour=Flavour.objects.get(pk=id)
    user_profile = CustomUser.objects.get(pk=request.user.pk)
    user_profile.balance+=flavour.quantity
    user_profile.save()

    flavour.delete()
    
    return redirect('list_flavour')

