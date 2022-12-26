from django.shortcuts import render , redirect
from django.http import HttpResponse
from . models import friends_List
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required
from django.views.decorators.csrf import csrf_protect
# Create your views here.

def index(request):
    return render(request,'index.html')
def JoinNow(request):
    if request.method == 'POST':
        First_Name = request.POST['First_Name']
        Last_Name = request.POST['Last_Name']
        WhatsappNumber = request.POST['WhatsappNumber']
        Phone_Number = request.POST['Phone_Number']

        # if friends_List.objects.filter(First_Name=First_Name).exists():
        #         return render(request, 'JoinNow.html', {'error': 'First_Name is already taken'})
        # elif friends_List.objects.filter(WhatsappNumber=WhatsappNumber).exists():
        #         return render(request, 'JoinNow.html', {'error': 'WhatsappNumber is already taken'})
        # else:
        #         friends_List = friends_List(First_Name=First_Name,Last_Name=Last_Name, WhatsappNumber=WhatsappNumber,Phone_Number=Phone_Number)
        #         friends_List.save()
                
        #         return redirect('index')
        if friends_List.objects.filter(First_Name=First_Name).exists():
            return render(request, 'JoinNow.html', {'error': 'First_Name is already taken'})
        elif friends_List.objects.filter(WhatsappNumber=WhatsappNumber).exists():
            return render(request, 'JoinNow.html', {'error': 'WhatsappNumber is already taken'})
            
        else:

            application = friends_List(First_Name=First_Name, Last_Name=Last_Name, WhatsappNumber=WhatsappNumber, Phone_Number=Phone_Number)
            application.save()

            return render(request, 'index.html', {'error': 'Thank you for Registation!'})
    return render(request,'JoinNow.html')
@login_required
def friendsReport(request):
    results=friends_List.objects.all();
    friendsReport={'friendsReport':results}
    return render(request,'friendsReport.html',friendsReport)
@login_required
@permission_required('school.delete_friends_List')
def delete (request,id):
    f=friends_List.objects.get(id=id)
    f.delete()
    return friendsReport(request)
@login_required
@permission_required('school.change_friends_List')
def update (request,id):
    if request.method == 'POST':
        First_Name = request.POST['First_Name']
        Last_Name = request.POST['Last_Name']
        WhatsappNumber = request.POST['WhatsappNumber']
        Phone_Number = request.POST['Phone_Number']

        results=friends_List.objects.get(id=id)
        
        results.First_Name=First_Name
        results.Last_Name=Last_Name
        results.WhatsappNumber=WhatsappNumber
        results.Phone_Number=Phone_Number
        results.save()
        friendsupdate={'friendsupdate':results}
        return render(request, 'index.html', {'error': 'Your details have been updated'})
    return render(request,'update.html')

def logout (request):
    return render(request,'LogOut.html')
