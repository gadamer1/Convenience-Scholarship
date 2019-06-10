from django.shortcuts import render,redirect
from .forms import SignUpForm,UserDetailForm,UserUniquenessForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from .models import Profile,UserUniqueness
from django.contrib.auth.forms import AuthenticationForm
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
    if request.method == 'POST': # If the form has been submitted...
        try :
            profile_instance = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            profile_instance = Profile(user= request.user)


        try :
            uniqueness_instance = UserUniqueness.objects.get(user=request.user)
        except UserUniqueness.DoesNotExist:
            uniqueness_instance = UserUniqueness(user= request.user)

        detail_form = UserDetailForm(request.POST,instance=profile_instance, prefix = "detail")
        uniqueness_form = UserUniquenessForm(request.POST,instance=uniqueness_instance, prefix = "uniqueness")
        if detail_form.is_valid() and uniqueness_form.is_valid(): # All validation rules pass
            detail =detail_form.save(commit=False)
            detail.user = request.user
            detail.save()
            uniqueness =uniqueness_form.save()
            uniqueness.user = request.user
            uniqueness.save()
            
            return redirect('scholarship:main')
    else:
        detail_form = UserDetailForm(prefix = "detail")
        uniqueness_form = UserUniquenessForm(prefix = "uniqueness")
    return render(request,'userauth/detail.html',{'detail_form':detail_form
            ,'uniqueness_form':uniqueness_form})


def logout_view(request):
    logout(request)
    return render(request,'scholarship/main.html')