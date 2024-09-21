from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserInfo
from .serializers import UserInfoSerializer
from core.getToken import getToken
from core.sendAUTH import sendAUTH
from core.authChecker import authChecker

class UserInfoView(APIView):
    def post(self, request):
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            toekndata =getToken()
            sendAUTH_data = sendAUTH(serializer.data,toekndata)
            authChecker_data=authChecker(sendAUTH_data)
            return Response(authChecker_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 