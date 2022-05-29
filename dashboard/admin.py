from django.contrib import admin
from dashboard.models import Users,Pooja,AssignPooja,expenses,income

# Register your models here.
admin.site.register(Users)
admin.site.register(Pooja)
admin.site.register(AssignPooja)
admin.site.register(expenses)
admin.site.register(income)

