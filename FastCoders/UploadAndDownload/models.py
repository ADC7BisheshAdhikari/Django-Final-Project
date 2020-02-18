from django.db import models

# Create your models here.
class CompanyManager(models.Manager):
    pass

class ApplicantProfile(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField(max_length=30)
    Mobile_No=models.IntegerField()
    Address=models.CharField(max_length=30)
    pdf=models.FileField(upload_to='CV/pdfs/')
    Objects= CompanyManager()

    def __str__(self):
        return f"{self.Name,self.Email,self.Mobile_No,self.Address,self.pdf}"

class Meta:
        db_table="ApplicantProfile" 
  

    
