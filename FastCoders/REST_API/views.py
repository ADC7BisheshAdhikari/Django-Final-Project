from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from easyjob.models import Company
import json

@csrf_exempt
def view_get_post_company(request):
    if request.method == "GET":
        company = Company.objects.all()
        list_of_company = list(company.values("cCompanyName","cVacantPost","cVacancyNumber","cEmail","cMobile","cLocation"))
        dictionary_name = {
        "company":list_of_company
    }
        return JsonResponse(dictionary_name)
        #Create
    elif request.method == "POST":
        python_dictionary_object = json.loads(request.body)
        get_cCompanyName=python_dictionary_object['cCompanyName']
        get_cVacantPost=python_dictionary_object['cVacantPost']
        get_cVacancyNumber=python_dictionary_object['cVacancyNumber']
        get_cEmail=python_dictionary_object['cEmail']
        get_cMobile=python_dictionary_object['cMobile']
        get_cLocation=python_dictionary_object['cLocation']
        company_obj = Company(cCompanyName=get_cCompanyName,cVacantPost=get_cVacantPost,cVacancyNumber=get_cVacancyNumber,cEmail=get_cEmail,cMobile=get_cMobile,cLocation=get_cLocation)
        company_obj.save()
    
        return JsonResponse({
            "message":"Successfully posted!!"
        })
    else:
        return HttpResponse("Other HTTP verbs testing")
    
@csrf_exempt
def view_getByID_updateByID_deleteByID(request,ID):
    print("What's the request =>",request.method)
    if request.method == "GET":
        com = Company.objects.get(id = ID)
        print(type(com.cCompanyName))
        return JsonResponse({
            "id":com.id,
            "cCompanyName":com.cCompanyName,
            "cVacantPost":com.cVacantPost,
            "cVacancyNumber":com.cVacancyNumber,
            "cEmail":com.cEmail,
            "cMobile":com.cMobile,
            "cLocation":com.cLocation
        })
    
    elif request.method=="PUT":
        com = Company.objects.get(id = ID)
        python_dictionary_object = json.loads(request.body)
        com.cCompanyName=python_dictionary_object['cCompanyName']
        com.cVacantPost=python_dictionary_object['cVacantPost']
        com.cVacancyNumber=python_dictionary_object['cVacancyNumber']
        com.cEmail=python_dictionary_object['cEmail']
        com.cMobile=python_dictionary_object['cMobile']
        com.cLocation=python_dictionary_object['cLocation']
        com.save()
        return JsonResponse({
        "message":" update successfully"
        })

    elif request.method == "DELETE":
        com = Company.objects.get(id = ID)
        com.delete()
        return JsonResponse({
        "message":" Deleted successfully"
        })
    
@csrf_exempt
def list_company_pagination(request,pagenumber,size):
    skip = size * (pagenumber - 1)
    company = Company.objects.all()[skip: (pagenumber * size)]
    data={"CompanyDetails": list(company.values("id","cCompanyName","cVacantPost","cVacancyNumber","cEmail","cMobile","cLocation")),}
    return JsonResponse({'company': data})


