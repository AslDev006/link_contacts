from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError
from .utility import *
from .models import *

class AllContantSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = "__all__"


class ContantSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = ["first_name", "last_name", "address", "phone_number", 'course_1', 'course_2', 'course_3']
    def validate_first_name(self, first_name):
        if len(first_name) < 3 or len(first_name) > 30:
            raise ValidationError(
                {
                    "message": "First name must be between 5 and 30 characters long",
                    "status": status.HTTP_400_BAD_REQUEST
                }
            )
        if first_name.isdigit():
            raise ValidationError(
                {
                    "message": "This First name is entirely numeric",
                    "status": status.HTTP_400_BAD_REQUEST
                }
            )
        return first_name

    def validate_last_name(self, last_name):
        if len(last_name) < 5 or len(last_name) > 30:
            raise ValidationError(
                {
                    "message": "Last name must be between 5 and 30 characters long",
                    "status": status.HTTP_400_BAD_REQUEST
                }
            )
        if last_name.isdigit():
            raise ValidationError(
                {
                    "message": "This Last name is entirely numeric",
                    "status": status.HTTP_400_BAD_REQUEST
                }
            )
        return last_name


    def validate_last_name(self, address):
        if len(address) < 5 or len(address) > 50:
            raise ValidationError(
                {
                    "message": "Address must be between 5 and 50 characters long",
                    "status": status.HTTP_400_BAD_REQUEST
                }
            )
        if address.isdigit():
            raise ValidationError(
                {
                    "message": "Address name is entirely numeric",
                    "status": status.HTTP_400_BAD_REQUEST
                }
            )
        return address

class TgContantSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = ["tg_id", "first_name", "last_name", "address", "phone_number", 'course_1', 'is_site']

    def validate_first_name(self, first_name):
        if len(first_name) < 3 or len(first_name) > 30:
            raise ValidationError(
                {
                    "message": "First name must be between 5 and 30 characters long",
                    "status": status.HTTP_400_BAD_REQUEST
                }
            )
        if first_name.isdigit():
            raise ValidationError(
                {
                    "message": "This First name is entirely numeric",
                    "status": status.HTTP_400_BAD_REQUEST
                }
            )
        return first_name


    def validate_last_name(self, last_name):
        if len(last_name) < 5 or len(last_name) > 30:
            raise ValidationError(
                {
                    "message": "Last name must be between 5 and 30 characters long",
                    "status": status.HTTP_400_BAD_REQUEST
                }
            )
        if last_name.isdigit():
            raise ValidationError(
                {
                    "message": "This Last name is entirely numeric",
                    "status": status.HTTP_400_BAD_REQUEST
                }
            )
        return last_name

    def validate_last_name(self, address):
        if len(address) < 5 or len(address) > 50:
            raise ValidationError(
                {
                    "message": "Address must be between 5 and 50 characters long",
                    "status": status.HTTP_400_BAD_REQUEST
                }
            )
        if address.isdigit():
            raise ValidationError(
                {
                    "message": "Address name is entirely numeric",
                    "status": status.HTTP_400_BAD_REQUEST
                }
            )
        return address