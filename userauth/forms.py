from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,UserUniqueness

class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='YYYY-MM-DD', label='생년월일')
    class Meta:
        model = User
        fields= ['username','password1','password2','birth_date']
        labels = {
            'username':'아이디',
            'password1':'비밀번호',
            'password2':'비밀번호 재확인'
        }
       


class UserDetailForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_grade','user_completion_semester','user_living_area',
        'user_income_level'
        ]
        labels ={
            'user_grade':'성적',
            'user_completion_semester':'수료한 학기',
            'user_living_area':'소재지',
            'user_income_level':'소득분위',
        }

class UserUniquenessForm(forms.ModelForm):
    class Meta:
        model = UserUniqueness
        fields = [
            'u_1','u_2','u_3','u_4','u_5','u_6',
            'u_7','u_8','u_9','u_10','u_11'
        ]
        labels={
            'u_1':'다문화가정','u_2':'기초생활수급자','u_3':'차상위계층','u_4':'장애인','u_5':'새터민','u_6':'보훈대상자',
            'u_7':'조부모가정','u_8':'다자녀','u_9':'한부모','u_10':'학생가장','u_11':'농어촌자녀'
        }