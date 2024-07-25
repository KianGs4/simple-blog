from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import userRegisterFrom, profileUpdateForm, userUpdateForm
from django.contrib.auth.decorators import login_required
 

def register(request):
    if request.method == 'POST': 
        form = userRegisterFrom(request.POST)
        if form.is_valid(): 
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account created successfully! You are now able to log in')
            return redirect('login')

    else:
        form = userRegisterFrom()
    return render(request, 'users/register.html', {'form' : form})

@login_required
def profile(request): 
    if request.method == 'POST': 
        u_form = userUpdateForm(request.POST, instance=request.user)
        p_form = profileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid(): 
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been updated successfully!')
            return redirect('profile')

    else: 
        u_form = userUpdateForm(instance=request.user)
        p_form = profileUpdateForm(instance=request.user.profile)

    context = {
        'uForm' : u_form,
        'pForm' : p_form
    }
    return render(request, 'users/profile.html', context)
