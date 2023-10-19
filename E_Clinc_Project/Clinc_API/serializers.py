from rest_framework import serializers
from Clinc_API.models import Gender, Clinic, Patient, \
    Session, Document, Doctor, BookingStatus, Booking, UsersSystem
from . import models


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ['gnd_id', 'gnd_name_en', 'gnd_name_ar']


class ClinicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clinic
        fields = ['id', 'cln_name_en', 'cln_name_ar']


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    # genders = GenderSerializer(many=False)

    class Meta:
        model = Patient
        fields = ['pnt_id', 'pnt_age', 'pnt_img_url', 'pnt_phone',
                  'pnt_email', 'pnt_gender', 'pnt_name_en', 'pnt_name_ar']
        # fields = ['pnt_id', 'pnt_age', 'pnt_img_url', 'pnt_phone',
        #           'pnt_email', 'pnt_pass', 'pnt_gender_id', 'pnt_status',
        #           'pnt_name_en', 'pnt_name_ar']
        # extra_kwargs = {
        #     'pnt_pass': {
        #         'write_only': True,
        #         'style': {'input_type': 'password'}
        #     }

    # def create(self, validated_data):
    #     """Create and return a new user"""
    #     patient = models.Patient.objects.create_user(
    #         validated_data['pnt_email'],
    #         validated_data['pnt_phone'],
    #         validated_data['pnt_name_en'],
    #         validated_data['pnt_pass'],
    #         validated_data['pnt_age'],
    #         validated_data['pnt_gender'],
    #         validated_data['pnt_status'],
    #         validated_data['pnt_name_ar'],
    #         validated_data['is_superuser'],
    #
    #     )
    #
    #     return patient


class UsersSysSerializer(serializers.HyperlinkedModelSerializer, serializers.ModelSerializer):
    # genders = GenderSerializer(many=False)
    class Meta:
        model = UsersSystem
        fields = ['password', 'usr_phone', 'usr_email', 'usr_age',
                  'usr_img_url', 'is_staff', 'is_active', 'usr_type',
                  'usr_gender', 'is_superuser', 'is_doctor', 'is_patient']
        # fields = ['pnt_id', 'pnt_age', 'pnt_img_url', 'pnt_phone',
        #           'pnt_email', 'pnt_pass', 'pnt_gender_id', 'pnt_status',
        #           'pnt_name_en', 'pnt_name_ar']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }

        }

    def create(self, validated_data):
        """Create and return a new user"""
        users = models.UsersSystem.objects.create_user(
            password=validated_data['password'],
            usr_phone=validated_data['usr_phone'],
            usr_email=validated_data['usr_email'],
            usr_age=validated_data['usr_age'],
            usr_img_url=validated_data['usr_img_url'],
            is_staff=validated_data['is_staff'],
            desc=validated_data['desc'],
            is_active=validated_data['is_active'],
            usr_type=validated_data['usr_type'],
            usr_gender=validated_data['usr_gender'],
            is_superuser=validated_data['is_superuser'],
            name_ar=validated_data['name_ar'],
            name_en=validated_data['name_en'],
            major=validated_data['major'],
            clinic=validated_data['clinic']

        )

        return users


class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = ['sin_id', 'sin_bok', 'sin_doc', 'sin_date']


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields = ['doc_id', 'doc_name_en', 'doc_name_ar', 'doc_url']


class DectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ['dct_major_id', 'dct_id', 'dct_name_en', 'dct_name_ar',
                  'dct_img_url', 'dct_desc', 'dct_phone', 'dct_pass', 'dct_gender', 'dct_clinic']
        extra_kwargs = {
            'dct_pass': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }


class BookingStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookingStatus
        fields = ['status_id', ' status_name_en', ' status_name_ar']


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ['bok_id', ' bok_dct', ' bok_pnt', 'bok_date', 'bok_status',
                  'bok_amt', 'bok_curr_id', 'bok_note']
