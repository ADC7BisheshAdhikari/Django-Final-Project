from django.urls import path
from UploadAndDownload import views

urlpatterns = [
    path('Applicantprofile/',views.profile_list, name="profileList"),
    path('upload',views.upload_cv, name="uploadprofile"),
]