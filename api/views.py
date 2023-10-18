from django.shortcuts import render
from rest_framework.response import Response
from .models import Company, Recruitment, User
from rest_framework.views import APIView
from .serializers import CompanySerializer, RecruitmentSerializer, UserSerializer, RecruitmentDetailSerializer
from rest_framework import status, filters
from django.shortcuts import get_object_or_404
from django.db.models import Q # filter에서 or를 사용하기 위해

class CompanyAPI(APIView):

    #회사 조회
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
    
class RecruitmentAPI(APIView):

    #채용 공고 조회
    def get(self, request):
        search = request.GET.get('search')
        
        if search == None:
            recruitments = Recruitment.objects.all()

        elif search.isdigit(): #search가 숫자라면
            search = int(search)
            queryset = Recruitment.objects.filter( Q(recruitment_id = search) | Q(compensation = search))
            recruitments = queryset  

        else: #search가 숫자가 아니라면
            queryset = Recruitment.objects.filter( Q(company_name = search) | Q(position = search)  
                                                  | Q(tech_stack = search))                         
            recruitments = queryset

        serializer = RecruitmentSerializer(recruitments, many=True)
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
        recruitments = Recruitment.objects.get(pk=pk)
        serializer = RecruitmentSerializer(recruitments, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #채용 공고 삭제
    def delete(self, request, pk):
        recruitments = Recruitment.objects.get(pk=pk)
        recruitments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserAPI(APIView):
     #유저 조회
    def get(self, request):
        Users = User.objects.all()
        serializer = UserSerializer(Users, many=True)
        return Response(serializer.data)
    
    #유저 생성
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RecruitmentDetailAPI(APIView):
    def get(self, request, pk):
        recruitment = get_object_or_404(Recruitment, pk=pk)
        serializer = RecruitmentDetailSerializer(recruitment)
        return Response(serializer.data)