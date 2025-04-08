import json

from django.http import JsonResponse, HttpRequest, HttpResponse
from .models import Company, Vacancy, Position
from django.views.decorators.csrf import csrf_exempt
from .serializers import CompanySerializer, VacancySerializer, PositionSerializer, PositionSerializer2

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

@csrf_exempt
def vacancies(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        vacancies_serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(vacancies_serializer.data, safe=False)

    if request.method == 'POST':
        new_vacancy = json.loads(request.body)
        Vacancy.objects.create(
            name=new_vacancy['name'],
            description=new_vacancy['description'],
            salary=new_vacancy['salary'],
            company=Company.objects.get(pk=new_vacancy['company']),
            position=Position.objects.get(pk=new_vacancy['position']),
        )
        return JsonResponse({"created": True}, safe=False, status=201)

        # serializer = VacancySerializer(data=new_vacancy)
        # if serializer.is_valid():
        #     serializer.save()
        #     return JsonResponse(serializer.data, status=201)

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

@csrf_exempt
def positions(request):
    if request.method == 'GET':
        positions = Position.objects.all()
        serializer = PositionSerializer(positions, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        new_position = json.loads(request.body)
        Position.objects.create(
            name=new_position['name'],
            description=new_position['description'],
        )
        return JsonResponse({"created": True}, safe=False, status=201)
        # return JsonResponse(serializer.data, status=201)
        # return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def position_details(request, id):
    try:
        position = Position.objects.get(pk=id)
    except Position.DoesNotExist as e:
        return JsonResponse({"message": str(e)}, status=404)

    if request.method == 'GET':
        position_serializer = PositionSerializer(position)
        return JsonResponse(position_serializer.data, safe=False)
    elif request.method == 'DELETE':
        position.delete()
        return JsonResponse({"message": "Position deleted!"})

    elif request.method == 'PUT':
        new_position = json.loads(request.body)
        # position.name = new_position['name']
        # position.description = new_position['description']
        # position.save()

        # return JsonResponse({"updated": True}, safe=False)

        serializer = PositionSerializer2(position, data=new_position)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
        #
        # serializer = PositionSerializer(instance=position, data=new_position)
        # if serializer.is_valid():
        #     serializer.save()
        #     return JsonResponse(serializer.data, status=201)
