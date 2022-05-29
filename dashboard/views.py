from io import RawIOBase
import logging
import base64
import re
import sys
import datetime, json
from datetime import date
from datetime import datetime, timedelta
from json import JSONEncoder
import json
from decimal import Decimal
from django.utils.dateparse import parse_date
from decimal import Decimal
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.db.models import Sum
from django.shortcuts import render , redirect
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.template import Context, Template
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
from django.contrib import messages
from django.core.paginator import EmptyPage, InvalidPage, Paginator
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.translation import get_language
from dashboard.models import Users, Pooja, AssignPooja, expenses , income
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from sree_vinayagar.encoders import DefaultEncoder
# Create your views here.


class home(View):
    template_name = "index.html"

    def get(self , request):     
        context = {}
        return render(request , self.template_name , context)


class users(View):
    template_name = "users.html"     
    
   
    def post(self , request):
        UserId = request.POST.get("userId")

        if(UserId == '0'):
            firstname = request.POST.get("firstname")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            address = request.POST.get("address")
            district = request.POST.get("district")
            dob = request.POST.get("dob")
            maritalstatus = request.POST.get("maritalstatus")
            marriagedate = request.POST.get("marriagedate")
            Status = request.POST.get("status")

            UsersDB = Users(
                name = firstname,
                email = email,
                phone = phone, #Username,
                address = address,
                district = district,
                dob = dob,
                maritalstatus = maritalstatus,
                marriagedate = marriagedate,
                status = Status,
            )

            UsersDB.save()
            messages.success(request , "User Added Successfully")

            return redirect("users")

        else:
            UserData = Users.objects.get(id = UserId)
            UserData.name = request.POST.get("firstname")
            UserData.email = request.POST.get("email")
            UserData.phone = request.POST.get("phone")
            UserData.address = request.POST.get("address")
            UserData.district = request.POST.get("district")
            UserData.dob = request.POST.get("dob")
            UserData.maritalstatus = request.POST.get("maritalstatus")
            UserData.marriagedate = request.POST.get("marriagedate")
            UserData.status = request.POST.get("status")

            UserData.save()    
            messages.success(request, "User Updated Successfully")

            return redirect("users")

    def get(self , request):
        Userdata = []
        UserObjects = Users.objects.all()

        for ht in UserObjects:
            data = {
                'id':ht.id,
                'name' : ht.name,
                'email' : ht.email,
                'phone':ht.phone,
                'address' : ht.address,
                'district' : ht.district,
                'dob' : str(ht.dob),
                'maritalstatus' : str(ht.maritalstatus),
                'marriagedate' : str(ht.marriagedate),
                'status' : ht.status,
            }
            Userdata.append(data)
        context = {
            "usersdata" : Userdata,
        }
        return render(request ,self.template_name , context)


class addRegion(View):
    template_name = "add_region.html"
  
    def post(self , request):
        if request.method == 'POST':
            
            PoojaId = request.POST.get("regionId")
            if PoojaId == '0':
                name = request.POST.get("name")
                desc = request.POST.get("desc")
                amount = request.POST.get("amount")

                PoojaDB = Pooja(
                    name = name,
                    desc = desc,
                    amount = amount,
                )

                PoojaDB.save()
                messages.success(request , "pooja Created Successfully")
                return redirect("pooja")

            else:
                PoojaData = Pooja.objects.get(id = PoojaId)
                PoojaData.name = request.POST.get("name")
                PoojaData.desc = request.POST.get("desc")
                PoojaData.amount = request.POST.get("amount")
                PoojaData.save()
                messages.success(request , "Pooja Updated Successfully")
                return redirect("pooja")


    def get(self , request):

        Poojadata = []
        PoojaObjects = Pooja.objects.all()

        for ht in PoojaObjects:
            data = {
                'id':ht.id,
                'name' : ht.name,
                'desc' : ht.desc,
                'amount':ht.amount,
            }
            Poojadata.append(data)
        context = {
            "poojadata" : Poojadata,
        }
        return render(request , self.template_name , context)


class assignRegion(View):
    template_name = "assign_region.html"

    def post(self , request):
        data = request.body
        
        if(data):
            AssignedRegionData = json.loads(data)['AssignedRegionData']
            
            for obj in AssignedRegionData:
                current_date = date.today()
                userObj = Users.objects.get(id = int(obj['userid']))
                poojaObj = Pooja.objects.get(id = int(obj['poojaid']))

                AssignedRegionDB = AssignPooja(
                    user_id = userObj,
                    pooja_id = poojaObj,
                    startdate = current_date,
                    status = 0,                    
                )

                AssignedRegionDB.save()

           
            messages.success(request , "Pooja Assigned Successfully")

            return JsonResponse({"status":"success"},status=200)

        return render(request ,self.template_name)

    def get(self , request):
        AssignPoojaData = []
        PoojaObjects = AssignPooja.objects.filter(status=0)

        for ht in PoojaObjects:
            UserData = Users.objects.get(id = ht.user_id.id)
            PoojaData = Pooja.objects.get(id = ht.pooja_id.id)                  
            data = {
                'id':ht.id,
                'username' : UserData.name,
                'poojaname' : PoojaData.name,
            }
            AssignPoojaData.append(data)
        context = {
            'AssignPoojaData' : AssignPoojaData,
            "poojadata" : Pooja.objects.all(),
            "userdata" : Users.objects.all(),
        }

        return render(request , self.template_name , context)


def removeRegion(request):

    data = request.body
        
    if(data):
        AssignedRegionData = json.loads(data)['AssignedRegionData'] 
        current_date = date.today()
        PoojaData = AssignPooja.objects.get(id = AssignedRegionData['id'])
        
        PoojaData.enddate = current_date
        PoojaData.status = 1

        PoojaData.save() 
        messages.success(request , "Pooja Updated Successfully")
        return redirect('assign_pooja')
    else:
        return JsonResponse({"error":"error"},status=403)
            
    return redirect('assign_pooja') 


# def expense(request):
#         if request.method == 'POST':
            
#             ExpenseID = request.POST.get("expenseId")
#             if ExpenseID == '0':
#                 date = request.POST.get("date")
#                 desc = request.POST.get("desc")
#                 amount = request.POST.get("amount")
#                 notes = request.POST.get("notes")

#                 expenseDB = expenses(
#                     date = date,
#                     description = desc,
#                     amount = amount,
#                     notes = notes
#                 )

#                 expenseDB.save()
#                 messages.success(request , "Expense is Successfully Added")
#                 return redirect("expense")

#         return render(request , 'expense.html')
        
class expense(View):
    template_name = "expense.html"

    def get(self , request):

        Expensedata = []
        ExpenseObjects = expenses.objects.all()

        for expenseValue in ExpenseObjects:
            data = {
                'id':expenseValue.id,
                'date' : expenseValue.date,
                'description' : expenseValue.description,
                'amount':expenseValue.amount,
                'notes':expenseValue.notes,
            }
            Expensedata.append(data)
        context = {
            "expensedata" : Expensedata,
        }
        return render(request , self.template_name , context)
  
    def post(self , request):
        if request.method == 'POST':
            
            ExpenseID = request.POST.get("expenseId")
            if ExpenseID == '0':
                date = request.POST.get("date")
                desc = request.POST.get("desc")
                amount = request.POST.get("amount")
                notes = request.POST.get("notes")

                print(date, desc, amount, notes)

                expenseDB = expenses(
                    date = date,
                    description = desc,
                    amount = amount,
                    notes = notes
                )

                expenseDB.save()
                messages.success(request , "Expense is Successfully Added")
                return redirect("expense")

                
        return render(request , self.template_name )




        
class incomes(View):
    template_name = "income.html"

    def get(self , request):

        IncomeData = []
        IncomeObject = income.objects.all()

        for IncomeValue in IncomeObject:
            data = {
                'id':IncomeValue.id,
                'date' : IncomeValue.date,
                'description' : IncomeValue.description,
                'amount':IncomeValue.amount,
                'notes':IncomeValue.notes,
            }
            IncomeData.append(data)
        context = {
            "incomedata" : IncomeData,
        }
        return render(request , self.template_name , context)
  
    def post(self , request):
        if request.method == 'POST':
            
            IncomeID = request.POST.get("incomeId")
            if IncomeID == '0':
                date = request.POST.get("date")
                desc = request.POST.get("desc")
                amount = request.POST.get("amount")
                notes = request.POST.get("notes")

                print(date, desc, amount, notes)

                IncomeDB = income(
                    date = date,
                    description = desc,
                    INamount = amount,
                    notes = notes
                )

                IncomeDB.save()
                messages.success(request , "Income is Successfully Added")
                return redirect("add_income")

                
        return render(request , self.template_name )

class Account(View):
    template_name = "account.html"

    def get(self, request):
        IncomeObj = income.objects.values()
        ExpenseObj = expenses.objects.values()
        context = {
            "expensedata" : ExpenseObj,
            "incomedata" : IncomeObj,
        }
        return render(request , self.template_name , context)

    def post(self , request):
        return render(request , self.template_name)

    

    