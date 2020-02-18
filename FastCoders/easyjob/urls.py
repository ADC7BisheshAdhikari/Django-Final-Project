from django.contrib import admin  
from django.urls import path  
from easyjob import views  
from .views import applicant, firstPage
from .views import *

urlpatterns = [   
    path('company/', views.emp, name="company"),  
    path('show',views.show, name="show"),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),
    path('search/',views.search, name="search"),
    path('base/',base,name="base"), 
    path('show/pagination/<int:SIZE>/<int:PAGENO>', views.list_company_pagination, name='list_company_pagination'), 

  
] 


urlpatterns += [
    path('profile/',applicant, name="profile"),
    path('profileTwo/',profileTwo, name="profileTwo"),
    path('',firstPage, name="index"),    
]


