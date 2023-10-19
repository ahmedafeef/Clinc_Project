# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import datetime
from typing import Any

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.html import mark_safe


class BookingStatus(models.Model):
    status_id = models.BigAutoField(primary_key=True)
    status_name_en = models.TextField()
    status_name_ar = models.TextField()

    class Meta:
        managed = True
        db_table = 'booking_status'


class Gender(models.Model):
    gnd_id = models.BigAutoField(primary_key=True)
    gnd_name_en = models.TextField()
    gnd_name_ar = models.TextField()

    class Meta:
        managed = True
        db_table = 'gender'

    def __str__(self):
        return self.gnd_name_en


class PaymentMethod(models.Model):
    pym_id = models.BigAutoField(primary_key=True)
    pym_name_en = models.TextField()
    pym_name_ar = models.TextField()

    class Meta:
        managed = True
        db_table = 'payment_method'

    def __str__(self):
        return self.pym_name_en


class UserProfileManager(BaseUserManager):
    """manager for user profiles"""

    def create_user(self, password, usr_phone, usr_email,
                    usr_age,
                    usr_img_url,
                    is_staff, desc,
                    is_active, usr_type, gender, is_superuser,
                    name_ar, name_en, major, clinic):
        """create a new user profile"""
        global doctor, patient
        if not usr_email:
            raise ValueError('Users must have an pnt_email address')
        elif not usr_phone:
            raise ValueError('Users must have an phone number')
        elif not password:
            raise ValueError('enter password')

        if major:
            major = Major.objects.get(major_id=major)

        if clinic:
            clinic = Clinic.objects.get(id=clinic)

        if gender:
            gender = Gender.objects.get(gnd_id=gender)

        # 1 =doctor 2=patient 3=stuff  4=admin

        if usr_type == 1:
            doctor = Doctor.objects.create(
                dct_name_en=name_en, dct_phone=usr_phone, dct_img_url=usr_img_url,
                dct_major=major, dct_gender=gender, dct_desc=desc,
                dct_clinic=clinic, dct_name_ar=name_ar)
            patient = None
        elif usr_type == 2:
            doctor = None
            patient = Patient.objects.create(
                pnt_age=usr_age,
                pnt_img_url=usr_img_url,
                pnt_phone=usr_phone,
                pnt_email=usr_email,
                pnt_gender=gender,
                pnt_name_ar=name_ar,
                pnt_name_en=name_en)
        elif usr_type == 3:
            patient = None
            doctor = None

        self.normalize_email(usr_phone)
        user = self.model(usr_phone=usr_phone, usr_email=usr_email,
                          major=major,
                          usr_age=usr_age, gender=gender,
                          usr_img_url=usr_img_url,
                          is_staff=is_staff, is_active=is_active, usr_type=usr_type,
                          is_doctor=doctor, is_patient=patient)
        user.set_password(password)
        user.is_superuser = is_superuser
        user.is_staff = is_staff
        user.save(using=self._db)

        return user

    def create_superuser(self, password, usr_phone, usr_email,
                         usr_age,
                         usr_img_url,
                         is_staff, desc,
                         is_active, usr_type, gender, is_superuser,
                         name_ar, name_en, major, clinic, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(password, usr_phone, usr_email,
                                usr_age,
                                usr_img_url,
                                is_staff, desc,
                                is_active, usr_type, gender, is_superuser,
                                name_ar, name_en, major, clinic)


class InsuranceCompanies(models.Model):
    insurance_number = models.BigAutoField(primary_key=True)
    company_name = models.TextField(max_length=100)
    phone_number = models.TextField(max_length=20, unique=True)
    email = models.EmailField()

    class Meta:
        managed = True
        db_table = "InsuranceCompanies"

    def __str__(self):
        return self.comp_name


class Patient(models.Model):
    pnt_id = models.BigAutoField(primary_key=True)
    pnt_age = models.IntegerField()
    pnt_img_url = models.TextField(blank=True)
    pnt_phone = models.TextField(unique=True)
    pnt_email = models.TextField(unique=True)
    pnt_gender = models.ForeignKey(Gender, models.DO_NOTHING)
    pnt_name_ar = models.TextField()
    pnt_isr_doc_img = models.ImageField(upload_to='images/pnt/', blank=True, null=True)
    pnt_name_en = models.TextField()
    has_insurance = models.BooleanField(default=False)
    pnt_insurance_num = models.CharField(max_length=50, unique=True, blank=True, null=True)
    pnt_insurance_co = models.ForeignKey(InsuranceCompanies, models.DO_NOTHING, blank=True, null=True)
    pnt_issue_date = models.DateField(blank=True, null=True)
    pnt_exp_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = "patient"

    def __str__(self):
        return self.pnt_name_en

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.pnt_isr_doc_img))

    image_tag.short_description = 'Pnt isr doc img'

    def image_tag_table(self):
        return mark_safe('<a href="/media/%s" width="80" height="80">insurance_img</a>' % (self.pnt_isr_doc_img))

    image_tag.short_description = 'Pnt isr doc img'


# payment from client  ====> insert to


class Services(models.Model):
    action = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Services'

    def __str__(self):
        return self.action

    def save(self, *args, **kwargs):
        if self.discount:
            self.discounted_price = self.price - (self.price * (self.discount / 100))
        else:
            self.discounted_price = None
        super().save(*args, **kwargs)


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=100)
    rcp_cst = models.ForeignKey(Patient, models.DO_NOTHING, blank=True, null=True)
    date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    currency = models.CharField(max_length=10, default='YER')

    def __str__(self):
        return self.invoice_number

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    srv_itm = models.ForeignKey(Services, on_delete=models.DO_NOTHING, related_name='srv_itm',
                                blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='YER')

    def __str__(self):
        return f'{self.srv_itm.action} - {self.invoice.invoice_number}'

    def save(self, *args, **kwargs):
        self.price = self.srv_itm.price
        super().save(*args, **kwargs)
        self.invoice.total_amount = sum(item.quantity * item.price for item in self.invoice.items.all())
        self.invoice.save()

    def delete(self, *args, **kwargs):
        invoice = self.invoice
        super().delete(*args, **kwargs)
        invoice.total_amount = sum(item.quantity * item.price for item in invoice.items.all())
        invoice.save()


class Receipt(models.Model):
    doc_serial = models.BigAutoField(primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=100)
    rcp_cst = models.ForeignKey(Patient, models.DO_NOTHING, blank=True, null=True)
    rcp_as_name = models.CharField(max_length=100, blank=True, null=True)
    payment_method = models.ForeignKey(PaymentMethod, models.DO_NOTHING, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    check_number = models.CharField(max_length=20, blank=True, null=True)
    invoice_number = models.CharField(max_length=20)
    transaction_number = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'receipt'


class Clinic(models.Model):
    id = models.BigAutoField(primary_key=True)
    cln_name_en = models.TextField()
    cln_name_ar = models.TextField()

    class Meta:
        managed = True
        db_table = 'clinic'

    def __str__(self):
        return self.cln_name_en


class Major(models.Model):
    major_id = models.BigAutoField(primary_key=True)
    major_name_ar = models.TextField()
    major_name_en = models.TextField()

    class Meta:
        managed = True
        db_table = 'major'

    def __str__(self):
        return self.major_name_en


class PracticingProfession(models.Model):
    practice_id = models.BigAutoField(primary_key=True)
    practice_number = models.CharField(max_length=30, blank=True, null=True)
    practicing_name = models.CharField(max_length=100)
    issue_date = models.DateField(blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PracticingProfession'

    def __str__(self):
        return self.practicing_name


class Doctor(models.Model):
    dct_id = models.BigAutoField(primary_key=True)
    dct_name_en = models.TextField()
    dct_desc = models.TextField()
    dct_img_url = models.TextField()
    dct_phone = models.TextField()
    dct_major = models.ForeignKey(Major, models.DO_NOTHING, blank=True, null=True)
    dct_gender = models.ForeignKey(Gender, models.DO_NOTHING, blank=True, null=True)
    dct_clinic = models.ForeignKey(Clinic, models.DO_NOTHING, blank=True, null=True)
    dct_name_ar = models.TextField()
    practicing_profession = models.ForeignKey(PracticingProfession, models.DO_NOTHING, null=True)

    class Meta:
        managed = True
        db_table = 'doctor'

    def __str__(self):
        return self.dct_name_en


class Booking(models.Model):
    bok_id = models.AutoField(primary_key=True)
    bok_dct = models.ForeignKey(Doctor, models.DO_NOTHING)
    bok_pnt = models.ForeignKey(Patient, models.DO_NOTHING)
    bok_date = models.DateTimeField(default=datetime.datetime.now)
    bok_status = models.ForeignKey(BookingStatus, models.DO_NOTHING)
    bok_amt = models.TextField()  # This field type is a guess.
    bok_curr_id = models.BigIntegerField(blank=True, null=True)
    bok_note = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'booking'


class Document(models.Model):
    doc_id = models.BigAutoField(primary_key=True)
    doc_name_en = models.TextField()
    doc_name_ar = models.TextField()
    doc_url = models.TextField()

    class Meta:
        managed = True
        db_table = 'document'


class UsersSystem(AbstractBaseUser, PermissionsMixin, models.Model):
    usr_id = models.BigAutoField(primary_key=True)
    usr_age = models.IntegerField()
    usr_img_url = models.TextField(blank=True)
    usr_phone = models.TextField(unique=True)
    usr_email = models.TextField(unique=True, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    desc = models.TextField(blank=True, null=True, default=None)
    name_ar = models.TextField(blank=True, null=True, default=None)
    name_en = models.TextField(blank=True, null=True, default=None)
    major = models.ForeignKey(Major, models.DO_NOTHING, null=True, default=None)
    is_active = models.BooleanField(default=True)
    gender = models.ForeignKey(Gender, models.DO_NOTHING, null=True, default=None)
    clinic = models.ForeignKey(Clinic, models.DO_NOTHING, null=True, default=None)
    usr_type = models.BigIntegerField()  # 1 =doctor 2=patient 3=stuff  4=admin
    is_superuser = models.BooleanField(default=False)
    is_doctor = models.ForeignKey(Doctor, models.CASCADE, blank=True, null=True, default=None)
    is_patient = models.ForeignKey(Patient, models.CASCADE, blank=True, null=True, default=None)

    objects = UserProfileManager()

    USERNAME_FIELD = "usr_phone"
    REQUIRED_FIELDS = ["usr_age", "is_staff", "is_active", "gender", "usr_type", "is_superuser",
                       'usr_email', 'usr_img_url', 'desc', 'name_ar', 'name_en', 'major', 'clinic'
                       ]

    class Meta:
        managed = True
        db_table = "users_system"

    def get_full_name(self):
        # Implement the logic to return the full name of the user
        return f"{self.name_ar} {self.name_en}"

    def get_phone(self):
        return self.usr_phone

    def get_email(self):
        return self.usr_email

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)


class Session(models.Model):
    sin_id = models.BigAutoField(primary_key=True)
    sin_bok = models.ForeignKey(Booking, models.DO_NOTHING)
    sin_doc = models.ForeignKey(Document, models.DO_NOTHING)
    sin_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'session'
