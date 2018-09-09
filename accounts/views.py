from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # log the user in
            return redirect('http://127.0.0.1:8000/order')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', { 'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user
            return redirect('http://127.0.0.1:8000/order')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})