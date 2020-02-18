from django.db import models


class CompanyManager(models.Manager):
    pass


class Company(models.Model):
    cCompanyName=models.CharField(max_length=100)
    cVacantPost=models.CharField(max_length=100)
    cVacancyNumber=models.IntegerField()
    cEmail=models.EmailField(max_length=100)
    cMobile=models.IntegerField()
    cLocation=models.CharField(max_length=50)
    objects= CompanyManager()

    def company_name_blank_check(self):
        return bool(self.cCompanyName)

    def company_name_list_check(self):
        list_of_company =c1.objects.all().count()
        return list_of_company 

    class Meta:
        db_table="Company"  
