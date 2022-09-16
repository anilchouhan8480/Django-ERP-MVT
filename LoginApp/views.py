from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.contrib.auth.models import Login
from django.contrib.auth.hashers import make_password
#from .models import Login_models, LoginRole
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Q
#from . forms import Login_forms
#from django.contrib.auth.models import Login
from django.contrib.auth import views as auth_views
from LoginApp.forms import User_forms
from django.contrib.auth.models import User





from django.contrib.auth.decorators import login_required




# Create your views here.
@login_required(login_url='/login')
def home(request):
	return render(request, "dashboard.html")

def user_login(request):
	print("checksys")
	if not request.user.is_authenticated:
		print("check6")
		if request.method=="POST":
			print("cheeck 5")
			fm=AuthenticationForm(request=request,data=request.POST)
			print("!!!")
			if fm.is_valid():
				print("check")
				uname=fm.cleaned_data['username']
				upass=fm.cleaned_data['password']
				user=authenticate(username=uname,password=upass)
				if user is not None:
					print("check3")

					login(request,user)
					messages.success(request,'Logged in successfully !!')
                    #return HttpResponseRedirect('/profile/')
					return redirect('/dashboard/')
		else:
			print("check1")
			fm=AuthenticationForm()
		return render(request,'login.html',{'form':fm})
	else:
		print("check4")
		return redirect('/dashboard/')

		#return render(request, "login.html",{'form':fm})

def Login(request):
	if request.method == "POST":
		un = request.POST['uname']
		pwd = request.POST['pwd']
		print("pwd:",pwd) 
		user = authenticate(username=un, password=pwd)

		if user.is_authenticated:
			login(request, user)
			#uObj = UserRole.objects.get(user__username=request.user)
			
			#if uObj.role == "4":
				#messages.success(request,'Login Success! Welcome. ')
				#print("employee admin role")
				#return redirect('/dashboard/')

			#elif uObj.role == "1":
				#messages.success(request,'Login Success! Welcome. ')
				#print("super admin role")
				#return redirect('/dashboard/')
			#print("Login success")
			#return redirect('/dashboard/')
		#else:
			#messages.error(request,'username or password not correct')
			#return render(request, "login.html",{'form':fm})

			#return redirect('/dashboard/')
	print("check")
	return render(request, "login.html")

def logout_call(request):
	print("adasdasdaDadADQAdd",request.method)
	#if request.method == 'POST':
	print(logout(request))	
	#return render(request, "login.html")
	return redirect('/login/')


'''def Create_User(request):
    form =User_forms()
    return render(request,'Create_User.html',{'form':form})

def user_forms(request):
    if request.method =='GET':
        form = User_forms()
        return render(request,'Create_User.html',{'form':form})
    
    else:
        form =User_forms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('User-list')'''

def Create_User(rqs):
    return  render(rqs, 'Create_User.html')		

def Create_User(request):
    if request.method == 'POST':
        print(request.POST)
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User Alredy Exist')
                return redirect('LoginApp/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Alredy Exist')
                return redirect('LoginApp')
            else:
                user = User.objects.create_user(username=username,
                                                email=email,
                                                password=password,first_name=first_name,last_name=last_name)
                user.save()
                return redirect('LoginApp')
        else:
            messages.info(request,'passwoed not matching...')
            return redirect('LoginApp')
            
    else:
        return render(request,'Create_User.html')
