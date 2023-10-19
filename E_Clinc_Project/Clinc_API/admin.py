from django import forms
from django.contrib import admin
from django.forms.utils import ErrorList
from modeltranslation.translator import register, TranslationOptions

from .models import Patient, Doctor, Booking, Major, InsuranceCompanies, UsersSystem, Clinic, Gender, PaymentMethod, \
    Services, PracticingProfession, Receipt, InvoiceItem, Invoice


class DoctorCustomView(admin.ModelAdmin):
    list_display = ('dct_id', 'dct_name_en', 'dct_name_ar', 'dct_phone', 'dct_gender', 'dct_clinic', 'dct_major',
                    'practicing_profession_id')


class PntCustomView(admin.ModelAdmin):
    # fields = ['pnt_age', 'pnt_phone', 'pnt_gender', 'pnt_name_ar', 'pnt_name_en', 'has_insurance', 'pnt_insurance_co',
    #           'pnt_insurance_num',
    #           'image_tag', 'pnt_isr_doc_img']
    fieldsets = (
        ("general", {"fields": ('pnt_age', 'pnt_phone', 'pnt_gender', 'pnt_name_ar', 'pnt_name_en',
                                )}),
        ("insurance", {"fields": ('pnt_insurance_num', 'image_tag', 'pnt_isr_doc_img', 'has_insurance')}),

    )

    #     ('has_insurance',
    #      {
    #          'fields': (),
    #          'classes': ('predefined',)
    #      }),
    #     (None, {
    #         'fields': ('pnt_insurance_co',),
    #         'classes': ('abcdefg',)
    #     })
    # )
    # form = PntModelForm

    list_display = ('pnt_name_ar',
                    'image_tag_table', 'pnt_age', 'pnt_phone', 'pnt_gender', 'pnt_name_en', 'has_insurance',
                    'pnt_insurance_num')

    readonly_fields = ['image_tag']


admin.site.register(Patient, PntCustomView)
admin.site.register(Doctor, DoctorCustomView)
admin.site.register(Booking)
admin.site.register(Major)
admin.site.register(Clinic)
admin.site.register(Gender)
admin.site.register(UsersSystem)
admin.site.register(InsuranceCompanies)
admin.site.register(Services)
admin.site.register(PracticingProfession)


class ReceiptAdminForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = '__all__'

    def __init__(self, data=None, files=None, auto_id="id_%s", prefix=None, initial=None, error_class=ErrorList,
                 label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None):
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance,
                         use_required_attribute, renderer)
        if self.instance.payment_method is 'bank988':
            self.fields.pop('bank_name')

        if self.instance.payment_method is 2:
            self.fields.pop('check_number')

    #
    # def __init__(self, type1=None, type2=None):
    #     super().__init__()
    #     if self.instance.payment_method is not 1:
    #         self.fields.pop('bank_name')
    #         self.fields.pop('check_number')
    #     elif self.instance.payment_method == 2:
    #         self.fields.pop('transaction_number')
    #     else:
    #         self.fields.pop('transaction_number')
    #         self.fields.pop('bank_name')
    #         self.fields.pop('check_number')


class PntAdminForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['pnt_isr_doc_img']

    def __init__(self, data=None, files=None, auto_id="id_%s", prefix=None, initial=None, error_class=ErrorList,
                 label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None):
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance,
                         use_required_attribute, renderer)

        if self.instance.payment_method is 'bank988':
            self.fields.pop('bank_name')

        if self.instance.payment_method is 2:
            self.fields.pop('check_number')

    #
    # def __init__(self, type1=None, type2=None):
    #     super().__init__()
    #     if self.instance.payment_method is not 1:
    #         self.fields.pop('bank_name')
    #         self.fields.pop('check_number')
    #     elif self.instance.payment_method == 2:
    #         self.fields.pop('transaction_number')
    #     else:
    #         self.fields.pop('transaction_number')
    #         self.fields.pop('bank_name')
    #         self.fields.pop('check_number')


class ReceiptAdmin(admin.ModelAdmin):
    form = ReceiptAdminForm
    # Add any other admin configuration you need


admin.site.register(Receipt, ReceiptAdmin)
admin.site.register(PaymentMethod)


@register(Doctor)
class DoctorTranslationOptions(TranslationOptions):
    fields = ('dct_desc',)


class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1



class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceItemInline]
    readonly_fields = ('total_amount',)


admin.site.register(Invoice, InvoiceAdmin)
