from django.contrib import admin
from .models import Contact
from .models import Customer
from .models import RegUsers
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
  list_display = ('id','ename', 'address','emailadd','num','message')
  
admin.site.register(Contact,ContactAdmin)



class CustomerAdmin(admin.ModelAdmin):
  list_display = ('id','customer_name', 'customer_address','customer_email','contact_number')
  
admin.site.register(Customer,CustomerAdmin)

class RegUsersAdmin(admin.ModelAdmin):
  list_display=('id','cName','cBranch','cNumber','cEmail','cUsername')
  
admin.site.register(RegUsers,RegUsersAdmin)