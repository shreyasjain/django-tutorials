from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, template_name='index.html')


def loginUser(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, template_name='login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')