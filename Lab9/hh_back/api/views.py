from django.shortcuts import render
import json
from django.http.response import HttpResponse, JsonResponse
from datetime import datetime, timedelta
import requests

from api.models import Company, Vacancy



def list_of_companies(request):
    # if request.method == 'GET':
    companies = Company.objects.all()
    companies_json = [p.to_json() for p in companies]
    return JsonResponse(companies_json,safe=False)


def company_detail(request, company_id):
    try:
        company = Company.objects.get(id = company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)
    # if request.method == 'GET':
    return JsonResponse(company.to_json(),safe=False)


def list_of_vacancies(request):
    # if request.method == 'GET':
    vacancies = Vacancy.objects.all()
    vacancies_json = [p.to_json() for p in vacancies]
    return JsonResponse(vacancies_json,safe=False)
        

def vacancy_detail(request,vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id = vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)
    # if request.method == 'GET':
    return JsonResponse(vacancy.to_json(),safe=False)

def vacancies_of_company(request, company_id):
    vacancies = Vacancy.objects.all()
    vacancies_json = [p.to_json() for p in vacancies]

    company = Company.objects.get(pk= company_id)
    matching_vacancies = []

    for vacancy in vacancies_json:
        if vacancy['company'] == company.id:
            matching_vacancies.append(vacancy)

    if len(matching_vacancies) != 0:
        return JsonResponse(matching_vacancies,safe=False,json_dumps_params={'indent':2})
    return JsonResponse({'error':'Vacancies not found'})

def top_ten_vacancies(request):
    vacancies = []
    for vacancy in Vacancy.objects.all():
        vacancies.append(vacancy.to_json())
    sorted_array = sorted(vacancies, key = lambda x : x['salary'], reverse= True)
    # vacancies.reverse()
    if(sorted_array.count != 0):
        return JsonResponse(sorted_array[0:11],safe=False,json_dumps_params={'indent':2})
    return JsonResponse({'error':'Error404'})
