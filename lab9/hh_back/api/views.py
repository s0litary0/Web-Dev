import json

from django.http import JsonResponse, HttpRequest, HttpResponse
from .models import Company, Vacancy
from django.views.decorators.csrf import csrf_exempt
from .serializers import CompanySerializer, VacancySerializer

from django.shortcuts import render

from .serializers import CompanySerializer


# Create your views here.
@csrf_exempt
def companies(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_serializer = CompanySerializer(companies, many=True)
        return JsonResponse(companies_serializer.data, safe=False)
    elif request.method == 'POST':
        new_company = json.loads(request.body)
        serializer = CompanySerializer(data=new_company)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

@csrf_exempt
def company_details(request, id):
    try:
        company = Company.objects.get(pk=id)
    except Company.DoesNotExist as e:
        return JsonResponse({"message": str(e)}, status=404)

    company_serializer = CompanySerializer(company)
    if request.method == 'GET':
        return JsonResponse(company_serializer.data, safe=False)
    else:
        ...

def company_vacancies(request, id):
    try:
        company = Company.objects.get(pk=id)
        vacancies = company.vacancies.all()
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)

    except Company.DoesNotExist as e:
        return JsonResponse({"message": str(e)}, status=404)

def vacancies(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        vacancies_serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(vacancies_serializer.data, safe=False)

def vacancy_details(request, id):
    try:
        vacancy = Vacancy.objects.get(pk=id)
        vacancy_serializer = VacancySerializer(vacancy)
        return JsonResponse(vacancy_serializer.data, safe=False)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({"message": str(e)}, status=404)

def top_ten_vacancies(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.order_by('-salary')[:10]
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)
