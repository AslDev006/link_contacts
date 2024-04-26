import environ
import os
import re
import threading
import phonenumbers
from django.template.loader import render_to_string
from rest_framework.exceptions import ValidationError



env = environ.Env()
environ.Env.read_env()
phone_regex = re.compile(env('phone'))

def check_phone_number(phone_number):
    phone_number = phonenumbers.parse(phone_number, None)
    if phonenumbers.is_valid_number(phone_number):
        phone_number = env("phone_number")
    else:
        data = {
            "success": False,
            'message': "Phone Number were an error, please try again."
        }
        raise ValidationError(data)
    print(" phone data :", phone_number)
    return phone_number


def check_first_name(first_name):
    regex_name = re.compile(r'^([a-z]+)( [a-z]+)*( [a-z]+)*( [.*]+)*$',
                            re.IGNORECASE)

    res = regex_name.search(first_name)
    if res:
        first_name = env('first_name')
    else:
        data = {
            "success": False,
            'message': "First name were an error, please try again."
        }
        print(" First data :", data)
        raise ValidationError(data)
    return first_name


def check_last_name(last_name):
    regex_name = re.compile(r'^([a-z]+)( [a-z]+)*( [a-z]+)*$',
                            re.IGNORECASE)

    res = regex_name.search(last_name)
    if res:
        last_name = env('last_name')
    else:
        data = {
            "success": False,
            'message': "Last name were an error, please try again."
        }
        print(" last data :", data)
        raise ValidationError(data)

    return last_name


def check_course_1(course_1):
    regex_name = re.compile(r'^[\w.-]+$',
                            re.IGNORECASE)

    res = regex_name.search(course_1)
    if res:
        last_name = env('course_1')
    else:
        data = {
            "success": False,
            'message': "First Course were an error, please try again."
        }
        print(" last data :", data)
        raise ValidationError(data)

    return last_name