from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from main.forms import Register_Form, Login_Form
from main.models import About




def index(request):
    user = User.objects.all()
    template_name = "index.html"
    return render(request, template_name, {"user":user})


def register(request):
    if request.method == 'POST':
        register_form = Register_Form(request.POST)

        if register_form.is_valid():

            email     =     register_form.cleaned_data['email']
            username  =  register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']

            if password1 == password2 :

                if User.objects.filter(username = username).exists():
                    messags.info(request, "username band, iltimos boshqa username dan foydalaning")
                    return redirect('register')

                elif User.objects.filter(email = email).exists():
                    messages.info(request, "Bunday email foydalanuvchisi mavjud")
                    return redirect('register')

                else:
                    user = User.objects.create_user(
                        username = username,
                        email = email,
                        password = password1
                    )
                    user.save()
                    user = auth.authenticate(username = username, password = password1)
                    auth.login(request, user)
                    return redirect('profile/'+username)
            else:
                messages.info(request, 'parollar bir-biriga mos emas')
                return redirect('register')
    else:
        register_form = Register_Form()
    return render(request, 'register.html', {'form' : register_form} )


def login(request):
    if request.method=='POST':
        login_form = Login_Form(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            
            user = auth.authenticate( username=username, password=password )

            if user != None:
                auth.login(request, user)
                return redirect('profile/'+username)
            else:
                messages.info(request, 'username yoki parol xato kiritildi')
                return redirect('login')
    else:
        login_form = Login_Form()
    return render(request, 'login.html', {'form':login_form})


def profile(request, username):
    template_name = "profile.html"
    return render(request, template_name)

def about(request):
    obj = About.objects.all()
    context = {
        'obj':obj[len(obj)-1]
    }
    template_name = "about.html"
    return render(request, template_name, context)

def logout(request):
    auth.logout(request)
    return redirect('/')