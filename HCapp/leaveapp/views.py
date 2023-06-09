from django.shortcuts import render
from .models import Leave_detail,LeaveApplication
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from members.models import Account
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    User_Account=Account.objects.get(user=request.user)
    AllApps=LeaveApplication.objects.filter(Account=User_Account)
    returnList=[]
    for application in AllApps:
        returnList.append(application)
    if (request.method =="POST"):
        User_Account=Account.objects.get(user=request.user)
        FromDate=request.POST["fromDate"]
        ToDate=request.POST["toDate"]
        Image=request.FILES.get("image")
        Description=request.POST["description"]
        Status="Pending"
        # img = Image(image)
        # img.save()
        leave = LeaveApplication(Account=User_Account,Status=Status)
        leave.Leave_details=Leave_detail(FromDate=FromDate,ToDate=ToDate,Prescription_Image=Image,Description=Description)
        leave.Leave_details.save()
        leave.save()
    return render(request,"leaveapp/leavebase.html",{"error":0,"Queue":returnList,})

@login_required
def Application_response(request):
    if request.method=="POST":
        action = request.POST.get('action') 
        id = request.POST.get('id')
        obj = get_object_or_404(LeaveApplication, id=id)
        print(action)
        if action == "accept":
            obj.Status="Approved"
            obj.save()
        elif action == "reject":
            obj.Status="Rejected"
            obj.save()
        return HttpResponseRedirect(reverse('ViewApplications'))
#else me error dena chahiye


#only for admin/DUGC
@login_required
def filterStatus(request):
    AllApps=LeaveApplication.objects.all()
    returnList=[]
    if(request.method =="GET"):
        action = request.GET.get("submit")
        if(action=="Approved"):
            for application in AllApps:
                if (application.Status=="Approved"):
                    returnList.append(application)
        else:
            for application in AllApps:
                if (application.Status=="Pending"):
                    returnList.append(application)
        previous_url = request.META.get('HTTP_REFERER')
        # return render(request,"leaveapp/ViewApplications.html",{
        #     "Queue":returnList,
        #     "Status":request.GET.get("ApplicationType"),
        passing={
            'Queue':returnList,
            "Status":action,
        }
        # return HttpResponseRedirect(f"{previous_url}?{'&'.join([f'{k}={v}' for k, v in passing.items()])}")
        return render(request,'leaveapp/ViewApplications.html',passing)

@login_required
def viewApplications(request):
    AllApps=LeaveApplication.objects.all()
    returnList=[]

    for application in AllApps:
        if (application.Status=="Pending"):
            returnList.append(application)
    return render(request,'leaveapp/ViewApplications.html',{
        "Queue":returnList,
        "Status":"Pending",
    })
    
## Give the selection of typeof applications name as Application Type



