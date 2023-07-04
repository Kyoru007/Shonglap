
from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignUpForm

def frontpage(request):
    return render(request, 'core/frontpage.html')


def signup(request):
    if request.method == 'POST':
        form =SignUpForm(request.POST)

        
        if form.is_valid():
            print("hi")
            user=form.save(commit=True)

            login(request, user)
            print("Hi")
            return redirect('frontpage')

    else:
        print("bi")
        form = SignUpForm()
    print("yo")
    return render(request, 'core/signup.html',{'form':form})