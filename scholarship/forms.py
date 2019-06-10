from django import forms
from . import models

class CreateScholarship(forms.ModelForm):
    class Meta:
        model = models.Scholar_content
        fields=['scholar_name','scholar_reward','scholar_needs','scholar_howto',
        'scholar_qna','scholar_recruitment_num','scholar_application_period',
        'scholar_foundation_name','scholar_who_draft','thumb_nail'
        ]

class CreateFilterScholarship(forms.ModelForm):
    class Meta:
        model = models.Scholar_fliter
        fields=[
            'filter_Grade','filter_completion_semester','filter_living_area',
            'filter_income_level','filter_is_our_college',
            'filter_uniqueness',
        ]

class CreateUniqueness(forms.ModelForm):
    class Meta:
        model = models.Uniqueness
        fields=[
            'u_1','u_2','u_3','u_4','u_5','u_6',
            'u_7','u_8','u_9','u_10','u_11'
        ]
