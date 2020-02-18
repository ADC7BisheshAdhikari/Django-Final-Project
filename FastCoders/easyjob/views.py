from django.shortcuts import render, redirect  
from easyjob.forms import CompanyForm  
from easyjob.models import Company  
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import Template,Context
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.contrib import messages

# Create your views here.  
#Create
def emp(request):  
    if request.method == "POST":  
        form = CompanyForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = CompanyForm()  
    return render(request,'company.html',{'form':form})  
#Read
def show(request):  
    employees = Company.objects.all()  
    return render(request,"show.html",{'employees':employees})  
def edit(request, id):  
    employee = Company.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
    #Update
def update(request, id):  
    employee = Company.objects.get(id=id)  
    form = CompanyForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
#Delete
def destroy(request, id):  
    employee = Company.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  





# Create your views here.
def search(request):#searching
    if request.method == "POST": 
        srch = request.POST['srh']

        if srch:
            match = Company.objects.filter(Q(cCompanyName__icontains=srch)|Q(cEmail__icontains=srch)|Q(cVacantPost__icontains=srch)|Q(cMobile__icontains=srch))


            if match:
                return render(request,'search.html',  {'object_list':match})
            else:
                 messages.error(request,'no result found')
               
        else:
            return HttpResponseRedirect('/search/')

    return render(request,'search.html')

def login(request):
    return render(request,'login.html')
def company(request):
    return render(request,'company.html')

#pagination
def list_company_pagination(request, SIZE, PAGENO):
    skip = SIZE * (PAGENO - 1)
    company = Company.objects.all()[skip: (PAGENO * SIZE)]
    return render(request, 'show.html', {'employees': company })



def applicant(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs= FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
    return render(request,'profile.html')

def firstPage(request):
    search = request.GET.get('search', False)
    if search:
        pass
    return render(request,'index.html')

def base(request):
    return render(request,'base.html')

def profileTwo(request):
     return render(request,'profileTwo.html')