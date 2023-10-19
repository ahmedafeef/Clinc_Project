# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ClincApiPatient(models.Model):
    pnt_id = models.BigAutoField(primary_key=True)
    pnt_name_en = models.TextField()
    pnt_age = models.IntegerField()
    pnt_img_url = models.TextField()
    pnt_phone = models.TextField()
    pnt_email = models.TextField(unique=True)
    pnt_pass = models.TextField()
    pnt_gender_id = models.BigIntegerField()
    pnt_status = models.BigIntegerField()
    pnt_name_ar = models.TextField()
    is_superuser = models.BooleanField()
    last_login = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'Clinc_API_patient'


class ClincApiPatientGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    patient = models.ForeignKey(ClincApiPatient, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Clinc_API_patient_groups'
        unique_together = (('patient', 'group'),)


class ClincApiPatientUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    patient = models.ForeignKey(ClincApiPatient, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Clinc_API_patient_user_permissions'
        unique_together = (('patient', 'permission'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(ClincApiPatient, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Booking(models.Model):
    bok_id = models.BigAutoField(primary_key=True)
    bok_dct = models.ForeignKey('Doctor', models.DO_NOTHING)
    bok_pnt = models.ForeignKey(ClincApiPatient, models.DO_NOTHING)
    bok_date = models.DateTimeField(blank=True, null=True)
    bok_status = models.ForeignKey('BookingStatus', models.DO_NOTHING)
    bok_amt = models.TextField()  # This field type is a guess.
    bok_curr_id = models.BigIntegerField(blank=True, null=True)
    bok_note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking'


class BookingStatus(models.Model):
    status_id = models.BigAutoField(primary_key=True)
    status_name_en = models.TextField()
    status_name_ar = models.TextField()

    class Meta:
        managed = False
        db_table = 'booking_status'


class Clinic(models.Model):
    id = models.BigAutoField(primary_key=True)
    cln_name_en = models.TextField()
    cln_name_ar = models.TextField()

    class Meta:
        managed = False
        db_table = 'clinic'


class Dector(models.Model):
    dct_id = models.BigAutoField(primary_key=True)
    dct_name_en = models.TextField()
    dct_major = models.ForeignKey('Major', models.DO_NOTHING, blank=True, null=True)
    dct_desc = models.TextField()
    dct_img_url = models.TextField()
    dct_phone = models.TextField()
    dct_pass = models.TextField()
    dct_gender = models.ForeignKey('Gender', models.DO_NOTHING)
    dct_clinic = models.ForeignKey(Clinic, models.DO_NOTHING, blank=True, null=True)
    dct_name_ar = models.TextField()

    class Meta:
        managed = False
        db_table = 'dector'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(ClincApiPatient, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Document(models.Model):
    doc_id = models.BigAutoField(primary_key=True)
    doc_name_en = models.TextField()
    doc_name_ar = models.TextField()
    doc_url = models.TextField()

    class Meta:
        managed = False
        db_table = 'document'


class Gender(models.Model):
    gnd_id = models.BigAutoField(primary_key=True)
    gnd_name_en = models.TextField(blank=True, null=True)
    gnd_name_ar = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gender'


class Major(models.Model):
    major_id = models.BigAutoField(primary_key=True)
    major_name_ar = models.TextField()
    major_name_en = models.TextField()

    class Meta:
        managed = False
        db_table = 'major'


class Session(models.Model):
    sin_id = models.BigAutoField(primary_key=True)
    sin_bok = models.ForeignKey(Booking, models.DO_NOTHING)
    sin_doc = models.ForeignKey(Document, models.DO_NOTHING)
    sin_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'session'
