from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.
def login(request):
    if request.method == 'POST':
        username_var1 = request.POST['username']
        password_var1 = request.POST['password']
        user = auth.authenticate(username=username_var1, password=password_var1)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')


def registration(request):
    if request.method == 'POST':
        username_var = request.POST['username']
        password_var = request.POST['password']
        cpassword_var = request.POST['password1']
        email_var = request.POST['email']
        firstname_var = request.POST['first_name']
        lastname_var = request.POST['last_name']
        if password_var == cpassword_var:
            if User.objects.filter(username=username_var).exists():
                messages.info(request, "Username already exist")
                return redirect('registration')
            elif User.objects.filter(email=email_var).exists():
                messages.info(request, "Email already exists")
                return redirect('registration')
            user = User.objects.create_user(username=username_var, password=password_var, email=email_var,
                                            first_name=firstname_var, last_name=lastname_var)
            user.save()
            return redirect('login')
            # print("registration completed")
        else:
            # print("Password not matched")
            messages.info(request, "Password not matched")
            return redirect('registration')
        return redirect('/')
    return render(request, 'registration.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
