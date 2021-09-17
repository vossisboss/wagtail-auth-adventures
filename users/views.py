from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect

def SignUpView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit = False)
            new_user.set_password(
                form.cleaned_data['password1'])
            new_user.save()
            return render(request,
                          'users/signup_done.html',
                          {'new_user': new_user})
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})