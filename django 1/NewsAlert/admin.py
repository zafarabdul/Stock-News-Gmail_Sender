from django.contrib import admin
from NewsAlert.models import Holder

class HolderAdmin(admin.ModelAdmin):
    list_display=('gmail','paswrd','st1','st2','st3','st4','st5')

admin.site.register(Holder,HolderAdmin)
