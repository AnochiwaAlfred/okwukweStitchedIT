<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from accounts.models import MyUser

# Create your views here.

def is_superuser(user):
    return user.is_superuser



def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('Correct')
            login_url = request.POST.get('next', '/') # get next page
            # login_url = next_page
            return redirect(login_url)
        
        else:
            print('Wrong Username or Password')
            return render(request, 'accounts/loginx.html', {'error_message': 'Invalid login credentials'})
    else:
        next_url = request.GET.get('next', '/') # get next page
        context = {'next_url':next_url}
        return render(request, 'accounts/loginx.html', context)
    

@login_required
def logoutView(request):
    try:
        logout(request)
    except:
        pass
    return render(request, 'accounts/logout.html')

def registerView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        profile_pics = request.POST.get('profile_pics')
        userCheck = MyUser.objects.filter(username=username)
        flag = False
        for i in userCheck:
            if i.username == username:
                flag = True
        if flag == True:
            print('User Already Exists')
            return render(request, 'accounts/register.html', {'error_message': 'User Already Exists'})
        else:
            if password1==password2:
                password = password1
                newUser = MyUser.objects.create_user(username=username, password=password, email=email)
                newUser.first_name = first_name
                newUser.last_name = last_name
                newUser.phone = phone
                newUser.gender = gender
                newUser.profile_pics = profile_pics
                newUser.save()
                return redirect('/')
            else: 
                print('Password Mismatch')
                return render(request, 'register.html', {'error_message': 'Password Mismatch'})
    else:
        next_url = request.GET.get('next', '/') # get next page
        context = {'next_url':next_url}
        return render(request, 'accounts/register.html', context)

def subscribeView(request):
    user = request.user
    newsLetterEmail = request.POST.get('newsLetterEmail')
    user.newsLetterSub = True
    user.newsLetterEmail = newsLetterEmail
    user.save()
    print('Successfully saved subscription email')
    return redirect('/')

@login_required
def profileView(request):
    user = request.user
    newsLetterEmail = request.POST.get('newsLetterEmail')
    user.newsLetterSub = True
    user.newsLetterEmail = newsLetterEmail
    user.save()
    print('Successfully saved subscription email')
=======
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from accounts.models import MyUser

# Create your views here.

def is_superuser(user):
    return user.is_superuser



def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('Correct')
            login_url = request.POST.get('next', '/') # get next page
            # login_url = next_page
            return redirect(login_url)
        
        else:
            print('Wrong Username or Password')
            return render(request, 'accounts/loginx.html', {'error_message': 'Invalid login credentials'})
    else:
        next_url = request.GET.get('next', '/') # get next page
        context = {'next_url':next_url}
        return render(request, 'accounts/loginx.html', context)
    

@login_required
def logoutView(request):
    try:
        logout(request)
    except:
        pass
    return render(request, 'accounts/logout.html')

def registerView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        profile_pics = request.POST.get('profile_pics')
        userCheck = MyUser.objects.filter(username=username)
        flag = False
        for i in userCheck:
            if i.username == username:
                flag = True
        if flag == True:
            print('User Already Exists')
            return render(request, 'accounts/register.html', {'error_message': 'User Already Exists'})
        else:
            if password1==password2:
                password = password1
                newUser = MyUser.objects.create_user(username=username, password=password, email=email)
                newUser.first_name = first_name
                newUser.last_name = last_name
                newUser.phone = phone
                newUser.gender = gender
                newUser.profile_pics = profile_pics
                newUser.save()
                return redirect('/')
            else: 
                print('Password Mismatch')
                return render(request, 'register.html', {'error_message': 'Password Mismatch'})
    else:
        next_url = request.GET.get('next', '/') # get next page
        context = {'next_url':next_url}
        return render(request, 'accounts/register.html', context)

def subscribeView(request):
    user = request.user
    newsLetterEmail = request.POST.get('newsLetterEmail')
    user.newsLetterSub = True
    user.newsLetterEmail = newsLetterEmail
    user.save()
    print('Successfully saved subscription email')
    return redirect('/')

@login_required
def profileView(request):
    user = request.user
    newsLetterEmail = request.POST.get('newsLetterEmail')
    user.newsLetterSub = True
    user.newsLetterEmail = newsLetterEmail
    user.save()
    print('Successfully saved subscription email')
>>>>>>> 4a8e8a410c304b57e382320e48a01d181f4dd41f
    return redirect('/')