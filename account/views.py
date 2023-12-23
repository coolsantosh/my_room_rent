from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer , LoginSerializer , UserProfileSerializer
from .models import User
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }





class RegisterView(APIView):
      def get(self,request,fomate=None):
             tasks = User.objects.all()
             serializer = UserRegisterSerializer(tasks, many = True)
             return Response(serializer.data)
      
      def post(self,request,fomate=None):
             serializer=UserRegisterSerializer(data=request.data)
             if serializer.is_valid(raise_exception=True):
                    user=serializer.save()
                  #   token = get_tokens_for_user(user)
                    return Response({'msg':'Registration success','token':token},status=status.HTTP_201_CREATED)  
             return Response({serializer.errors},status=status.HTTP_400_BAD_REQUEST)       
         

class LoginView(APIView):
      def post(self,request,fomate=None):
            serializer = LoginSerializer(data=request.data)

            if serializer.is_valid(raise_exception=True):
                  email = serializer.data.get('email')
                  password = serializer.data.get('password')
                  print(email),
                  print(password)
                  user = authenticate(email=email,password=password)
                  token= get_tokens_for_user(user)
                  return  Response({"message":"Login Successful","token":token},status=status.HTTP_200_OK)  
            else:
                  return Response({"message":"Login failed"},status=status.HTTP_404_NOT_FOUND) 
                    


class UserProfileView(APIView):
      permission_classes=[IsAuthenticated]
      def get(self,request,fomat=None):
            serializer= UserProfileSerializer(request.user)
            print(serializer.data)
            return Response(serializer.data,status=status.HTTP_200_OK)                        


      