from django.urls import path
from .views import view_get_post_company
from .views import view_getByID_updateByID_deleteByID
from .views import *

urlpatterns = [
    path('companyapis/',view_get_post_company),
    path('companyapis/<int:ID>',view_getByID_updateByID_deleteByID),
    path('show/<int:pagenumber>/<int:size>', list_company_pagination, name='list_company_pagination'), 
]