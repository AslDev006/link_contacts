import environ
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django_ratelimit.decorators import ratelimit
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .start_bot import get_post
from .utility import *
from .models import *
from .serializers import *
env = environ.Env()
environ.Env.read_env()
class ContactCreateView(APIView):
    permission_classes = [AllowAny, ]
    serializer_class = ContantSerializers

    @csrf_exempt
    # @ratelimit(key='request', rate='1/s')
    def post(self, request, *args, **kwargs):
        serializer = ContantSerializers(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data.get("phone_number")
            first_name = serializer.validated_data.get("first_name")
            last_name = serializer.validated_data.get("last_name")
            course_1 = serializer.validated_data.get("course_1")

        if check_phone_number(phone_number) == env('phone_number') and check_first_name(first_name) == env('first_name') and check_last_name(last_name) == env('last_name') and check_course_1(course_1) == env('course_1'):
            serializer.save()
            get_post(serializer.data)
            return JsonResponse({
                "success": True,
                "message": "Sent successfully !!!",
                "data": serializer.data
                }, status=200)
        else:
            return JsonResponse({
                "success": False,
                "message": "Sent unsuccessfully !!!",
                }, status=400)


@api_view(['GET', 'POST'])
@permission_classes((AllowAny, ))
def TgContactCreateView(request):
    if request.method == 'GET':
        snippets = ContactModel.objects.filter(is_site=False)
        serializer = TgContantSerializers(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TgContantSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                "success": True,
                "message": "Sent successfully !!!",
                "data": serializer.data
            }, status=200)
        return JsonResponse({
            "success": False,
            "message": "Sent unsuccessfully !!!",
        }, status=400)



@api_view(['GET'])
@permission_classes((AllowAny, ))
def TgContactDetailView(request, tg_id):
    try:
        user = get_object_or_404(ContactModel, tg_id=tg_id, is_site=False)
    except ContactModel.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AllContantSerializers(user)
        return JsonResponse({
            "success": True,
            "data": serializer.data
        }, status=200)