
# from users.forms import SignUpForm

from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm,ProfileUpdateForm,UserRegisterForm
from django.core.mail import send_mail
from .forms import ContactForm
from django.template.loader import render_to_string

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request,f'Account created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# login view 
# def login_request(request):
# 	if request.method == "POST":
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				login(request, user)
# 				messages.info(request, f"You are now logged in as {username}.")
# 				return redirect('index')
# 			else:
# 				messages.error(request,"Invalid username or password.")
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	form = AuthenticationForm()
# 	return render(request=request, template_name="registration/login.html", context={"login_form":form})      



def profile(request):

    title = 'Profile'
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,
                                   instance=request.user.profile)
        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
        messages.success(request,f'Update successful')
        return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'title':title,
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html',context)

def email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        
        if form.is_valid():
           
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            html = render_to_string('users/emails/contactform.html',{
                'name': name,
                'email': email,
                'content': content
            })
            print('the form was valid')
            send_mail('The contact form subject', 'This is the message','cenciousdev2022@gmail.com',['kancencious@gmail.com'], html_message=html)
            return redirect('email')
    else:
        form = ContactForm()
    return render(request, 'users/email.html',{'form': form})
