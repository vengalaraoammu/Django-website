from django.contrib import admin
from school.models import friends_List

class friends_ListAdmin(admin.ModelAdmin):
    list_display=['First_Name','Last_Name','WhatsappNumber','Phone_Number']

# Register your models here.
admin.site.register(friends_List)