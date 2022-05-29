from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 100 , null = True,)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length = 15 , null = True)
    address = models.CharField(max_length = 200 , null = True)
    district = models.CharField(max_length = 200 , null = True)
    dob = models.DateTimeField(auto_now=False , auto_now_add = False , null = True)
    maritalstatus = models.CharField(max_length = 200 , null = True)
    marriagedate = models.DateTimeField(auto_now=False , auto_now_add = False , null = True)
    status = models.IntegerField(default = 0)
    
    class Meta:
        verbose_name_plural = "Users"
        ordering = ['id']
        default_permissions = ()

class Pooja(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 200 , null = True)
    desc = models.CharField(max_length = 200 , null = True)
    amount = models.CharField(max_length = 200 , null = True)

    class Meta:
        verbose_name_plural = "Pooja"
        ordering = ['id']
        default_permissions = ()

class AssignPooja(models.Model):
    id = models.IntegerField(primary_key = True)
    pooja_id = models.ForeignKey(Pooja, on_delete=models.CASCADE , null = True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE , null = True)
    startdate = models.DateTimeField(auto_now=False , auto_now_add = False , null = True)
    enddate = models.DateTimeField(auto_now=False , auto_now_add = False , null = True)
    status = models.IntegerField(default = 0)

    class Meta:
        verbose_name_plural = "AssignPooja"
        ordering = ['id']
        default_permissions = ()

class expenses(models.Model):
    id = models.IntegerField(primary_key = True)
    date = models.DateField(auto_now=False , auto_now_add = False , null = True)
    description = models.TextField(blank=True)
    amount = models.IntegerField()
    notes = models.TextField(blank=True , null = True) 

class income(models.Model):
    id = models.IntegerField(primary_key = True)
    date = models.DateField(auto_now=False , auto_now_add = False , null = True)
    description = models.TextField(blank=True)
    amount = models.IntegerField()
    notes = models.TextField(blank=True , null = True) 

class account(models.Model):
    id = models.IntegerField(primary_key = True)
    Income = models.IntegerField()
    Expense = models.IntegerField()
    Balance = models.IntegerField()