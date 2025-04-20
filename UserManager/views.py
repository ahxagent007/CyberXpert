from django.shortcuts import render, redirect
from .forms import UserAccountForm
from .models import UserAccount
from .decorators import login_access_only, admin_access_only
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from django.contrib import messages

def Login(request):

    if request.method == 'POST':
        # Login user
        data = request.POST
        email = data['email']
        password = data['password']
        exists = UserAccount.objects.filter(email=email).exists()

        if not exists:
            # show message ('This Member does not exist')
            context = {
                'error_message' : 'This User does not exist'
                    }
            return render(request, 'user/login.html', context)

        #user = UserAccount.objects.get(email=email)
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            # Login Successful
            request.session['User_role'] = user.role
            request.session["User_id"] = user.id
            request.session["user_name"] = user.name

            user.last_login = datetime.now()
            user.save()

            messages.success(request, "Login successful")

            return redirect('Dashboard:Dashboard')

        else:
            context = {
                'error_message': 'Wrong Password. Please Check Again'
            }
            return render(request, 'user/login.html', context)

    else:
        context = {

        }
        return render(request, 'user/login.html', context)

@login_access_only()
def Logout(request):
    request.session['User_role'] = None
    request.session["User_id"] = None
    request.session["User_name"] = None

    logout(request)

    return redirect('UserManager:Login')

@admin_access_only()
def CreateUser(request):
    if request.method == 'POST':
        form = UserAccountForm(request.POST)
        if form.is_valid():
            #form.save()
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')

            user_obj = UserAccount.objects.create_user(name=name, email=email, password=password)
            return redirect('UserManager:UserList')  # Redirect to a view that shows all books
    else:
        form = UserAccountForm()
    return render(request, 'user/user_add.html', {'form': form})

@admin_access_only()
def UserList(request):
    all_user = UserAccount.objects.all()
    
    return render(request, 'user/user_list.html', {'all_user':all_user})