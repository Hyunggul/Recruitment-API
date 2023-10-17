from django.shortcuts import render
from rest_framework.response import Response
from .models import Company, Recruitment, User
from rest_framework.views import APIView
from .serializers import CompanySerializer, RecruitmentSerializer, UserSerializer
from rest_framework import status

class CompanyAPI(APIView):

    #회사 조회
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
    
class RecruitmentAPI(APIView):

    #채용 공고 조회
    def get(self, request):
        companies = Recruitment.objects.all()
        serializer = RecruitmentSerializer(companies, many=True)
        return Response(serializer.data)
    
    #채용 공고 생성
    def post(self, request):
        serializer = RecruitmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #채용 공고 수정(업데이트)
    def put(self, request, pk):
        companies = Recruitment.objects.get(pk=pk)
        serializer = RecruitmentSerializer(companies, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #채용 공고 삭제
    def delete(self, request, pk):
        recruitment = Recruitment.objects.get(pk=pk)
        recruitment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserAPI(APIView):
     #유저 조회
    def get(self, request):
        companies = User.objects.all()
        serializer = UserSerializer(companies, many=True)
        return Response(serializer.data)
    
    #유저 생성
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)