from django.shortcuts import render
from django.shortcuts import redirect
from .forms import ApplicantProfileForm
from .models import ApplicantProfile
from UploadAndDownload.models import ApplicantProfile 

# Create your views here.
#Download CV
def profile_list(request):
    profile= ApplicantProfile.Objects.all()
    return render(request,'ApplicantBio.html',{'profile':profile})

#Upload Cv
def upload_cv(request):
    if request.method == 'POST':
        form = ApplicantProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form =ApplicantProfileForm()
    return render(request,'profileTwo.html',{'form':form})

