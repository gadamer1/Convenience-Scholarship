from django.shortcuts import render,redirect
from .forms import SignUpForm,UserDetailForm,UserUniquenessForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from .models import Profile,UserUniqueness
from django.contrib.auth.forms import AuthenticationForm
from django.core import serializers
from django.forms import ModelForm
# Create your views here.

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else :
                return redirect('scholarship:main')
    else:
        form = AuthenticationForm()
    return render(request,'userauth/login.html',{'form':form})


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')           
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('userauth:detail')
    else:
        form = SignUpForm()
    return render(request,'userauth/signup.html',{'form':form})

@login_required(login_url ='login/login/')
def detail_view(request):
    try :
        uniqueness_instance = UserUniqueness.objects.get(u_ID=request.user)
    except UserUniqueness.DoesNotExist:
        uniqueness_instance = UserUniqueness(u_ID= request.user)
    try:
        profile_instance = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile_instance = Profile(user= request.user)
        
    if request.method == 'POST': # If the form has been submitted...
        detail_form = UserDetailForm(request.POST,instance=profile_instance, prefix = "detail")
        uniqueness_form = UserUniquenessForm(request.POST,instance=uniqueness_instance, prefix = "uniqueness")
        if detail_form.is_valid() and uniqueness_form.is_valid(): # All validation rules pass
            detail =detail_form.save(commit=False)
            detail.user = request.user
            detail.save()
            uniqueness =uniqueness_form.save()
            uniqueness.user = request.user
            uniqueness.save()
            return redirect('userauth:detail')
    else:
        detail_form = UserDetailForm(prefix = "detail",instance=profile_instance)
        uniqueness_form = UserUniquenessForm(prefix = "uniqueness",instance=uniqueness_instance)
    
    class UserShowForm(ModelForm):
        class Meta:
            model =UserUniqueness
            fields =('u_1','u_2','u_3','u_4','u_5',
            'u_6','u_7','u_8','u_9','u_10','u_11'
            )
            labels={
            'u_1':'다문화가정','u_2':'기초생활수급자','u_3':'차상위계층','u_4':'장애인','u_5':'새터민','u_6':'보훈대상자',
            'u_7':'조부모가정','u_8':'다자녀','u_9':'한부모','u_10':'학생가장','u_11':'농어촌자녀'
        }

    user_detail_form =UserShowForm(instance=uniqueness_instance)
    

    return render(request,'userauth/detail.html',{'detail_form':detail_form
            ,'uniqueness_form':uniqueness_form ,'user_detail_form':user_detail_form})


def logout_view(request):
    logout(request)
    return render(request,'scholarship/main.html')