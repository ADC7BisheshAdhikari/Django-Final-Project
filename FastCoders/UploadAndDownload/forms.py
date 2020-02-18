from django import forms
from.models import ApplicantProfile

class ApplicantProfileForm(forms.ModelForm):
    class Meta:
        model = ApplicantProfile
        fields =( 'Name','Email','Mobile_No','Address','pdf')