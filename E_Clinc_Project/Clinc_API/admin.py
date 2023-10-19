from django.contrib import admin

from Clinc_API.models import Patient, Doctor, Booking, Major, UsersSystem, Clinic, Gender

from modeltranslation.translator import register, TranslationOptions


class DoctorCustomView(admin.ModelAdmin):
    list_display = ('dct_id', 'dct_name_en', 'dct_name_ar', 'dct_phone', 'dct_gender', 'dct_clinic', 'dct_major')


admin.site.register(Patient)
admin.site.register(Doctor, DoctorCustomView)
admin.site.register(Booking)
admin.site.register(Major)
admin.site.register(Clinic)
admin.site.register(Gender)
admin.site.register(UsersSystem)


@register(Doctor)
class DoctorTranslationOptions(TranslationOptions):
    fields = ('dct_desc',)
