# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from typing import Any

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
import datetime


class BookingStatus(models.Model):
    status_id = models.BigAutoField(primary_key=True)
    status_name_en = models.TextField()
    status_name_ar = models.TextField()

    class Meta:
        managed = False
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


class Patient(models.Model):
    pnt_id = models.BigAutoField(primary_key=True)
    pnt_age = models.IntegerField()
    pnt_img_url = models.TextField(blank=True)
    pnt_phone = models.TextField(unique=True)
    pnt_email = models.TextField(unique=True)
    pnt_gender = models.ForeignKey(Gender, models.DO_NOTHING)
    pnt_name_ar = models.TextField()
    pnt_name_en = models.TextField()

    class Meta:
        managed = True
        db_table = "patient"

    def __str__(self):
        return self.pnt_name_en


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

    class Meta:
        managed = True
        db_table = 'doctor'


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
        managed = False
        db_table = 'booking'


class Document(models.Model):
    doc_id = models.BigAutoField(primary_key=True)
    doc_name_en = models.TextField()
    doc_name_ar = models.TextField()
    doc_url = models.TextField()

    class Meta:
        managed = False
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
        managed = False
        db_table = 'session'
