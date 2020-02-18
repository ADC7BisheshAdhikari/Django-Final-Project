from django.test import TestCase
from easyjob.models import Company 
# Create your tests here.

class CompanyTestCase(TestCase):
    #To check Blank
    def test_company_name_blank_check(self):
        c1=Company.objects.create(cCompanyName="Herald", cEmail="herald@heraldcollege.edu.np", cMobile=9800000000,cVacancyNumber=1)
        self.assertTrue(c1.company_name_blank_check())

    def test_company_name_check(self):
         c1=Company.objects.create(cCompanyName="Ram", cEmail="herald@heraldcollege.edu.np", cMobile=9800000000,cVacancyNumber=1)
         self.assertEqual(c1.cCompanyName, "Ram")


    
    def test_company_name_list_check(self):
        c1=Company.objects.create(cCompanyName="Ram", cEmail="herald@heraldcollege.edu.np", cMobile=9800000000,cVacancyNumber=1)
        self.assertEqual(c1.company_name_list_check(),1)