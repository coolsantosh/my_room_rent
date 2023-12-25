from django.shortcuts import render
from rest_framework import status
from .models import Room ,ROOM_TYPE_CHOICES ,  DISTRICT_CHOICE,STATUS_CHOICES 
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RoomSerializer
from rest_framework.permissions import IsAuthenticated



# Create your views here.

class RoomView(APIView):
    def get(self,request,format=None):
        district = request.GET.get('district')
        print(district)
        roomlist= Room.objects.filter(district=district)
        serializer= RoomSerializer(roomlist,many=True)
        print(roomlist)
        return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
    
    # permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class RoomTypeView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self,request,formate=None):
         return Response({'status':'success','data':[r_type[0] for r_type in ROOM_TYPE_CHOICES]},status=status.HTTP_200_OK)

class RoomStatusView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self,request,formate=None):
         return Response({'status':'success','data':[s_choice[0] for s_choice in STATUS_CHOICES]},status=status.HTTP_200_OK)

class RoomDistrictView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self,request,formate=None):
         return Response({'status':'success','data':[d_choice[0] for d_choice in DISTRICT_CHOICE]},status=status.HTTP_200_OK)

class RoomDetailView(APIView):
    def get(self,request,pk,format=None):
        roomlist= Room.objects.get(id=pk)
        serializer= RoomSerializer(roomlist)
        print(roomlist)
        return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
    
# class RoomPostByUser(APIView):
#     def get(self,request,format=None):
#         user = self.request.user
#         print(user)
#         room = Room.objects.filter(user=user)   
#         serializer = RoomSerializer(room, many=True) 
#         return Response(serializer.data, status=status.HTTP_200_OK)