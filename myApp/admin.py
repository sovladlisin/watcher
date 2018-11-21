from django.contrib import admin
from myApp.models import Patient, PatientList, Wing, UserProfileInfo, PatientLog


class PatientAdmin(admin.ModelAdmin):
    model = Patient

class PatientListAdmin(admin.ModelAdmin):
    model = PatientList

class WingAdmin(admin.ModelAdmin):
    model = Wing

class UserProfileInfoAdmin(admin.ModelAdmin):
    model = UserProfileInfo

class PatientLogAdmin(admin.ModelAdmin):
    model = PatientLog


admin.site.register(Patient, PatientAdmin)
admin.site.register(PatientList, PatientListAdmin)
admin.site.register(PatientLog, PatientLogAdmin)
admin.site.register(Wing, WingAdmin)
admin.site.register(UserProfileInfo,UserProfileInfoAdmin)