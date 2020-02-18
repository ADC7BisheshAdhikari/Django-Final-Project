from django.db import models

# Create your models here.
class Company(models.Model):
    CompanyName=models.CharField(max_length=20)
    Company_Email=models.EmailField(max_length=30)
    Mobile_No=models.IntegerField()
    Company_Location=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.CompanyName,self.Company_Email,self.Mobile_No,self.Company_Location}"


class Applicant(models.Model):
    Applicant_Name=models.CharField(max_length=20)
    Applicant_Email=models.EmailField(max_length=30)
    Applicant_Mobile_No=models.IntegerField()
    Applicant_address=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.Applicant_Name,self.Applicant_Email,self.Applicant_Mobile_No,self.Applicant_address}"

class Job(models.Model):
    Employer=models.ForeignKey(Company,on_delete=models.CASCADE)
    Jobseeker=models.ManyToManyField(Applicant,blank=True,related_name="jobseeker")
    Vacent_post=models.CharField(max_length=100)
    Vacency_no=models.IntegerField()



    def __str__(self):
        return f"{self.Employer,self.Jobseeker,self.Vacent_post,self.Vacency_no}"

class Resume(models.Model):
    Employee=models.ForeignKey(Applicant,on_delete=models.CASCADE )
    Education=models.TextField(max_length=40)
    Experience =models.TextField(max_length=40)

    def __str__(self):
        return f"{self.Employee,self.Education,self.Experience}"

class Profile(models.Model):
    Applicant_Profile=models.OneToOneField(Applicant,  on_delete = models.CASCADE, primary_key = False)