from django.shortcuts import render
import json
from django.http.response import HttpResponse, JsonResponse
from datetime import datetime, timedelta
import requests

from api.models import Company, Vacancy



def list_of_companies(request):
    companies = []
    for company in Company.objects.all():
        companies.append(company.to_json())
    return JsonResponse(companies,safe=False,json_dumps_params={'indent':2})

def company_detail(request, company_id):
    companies = []
    
    for company in Company.objects.all():
        companies.append(company.to_json())
        
    for company in companies:
        # print(company[id])
        if company['id'] == company_id:
            return JsonResponse(company,safe=False,json_dumps_params={'indent':2})
        
    return JsonResponse({'error':'Company not found'})


def list_of_vacancies(request):
    vacancies = []
    for vacancy in Vacancy.objects.all():
        vacancies.append(vacancy.to_json())
    return JsonResponse(vacancies,safe=False,json_dumps_params={'indent':2})

def vacancy_detail(request,vacancy_id):
    vacancies = []
    for vacancy in Vacancy.objects.all():
        vacancies.append(vacancy.to_json())
    for vacancy in vacancies:
        if vacancy['id'] == vacancy_id:
            return JsonResponse(vacancy,safe=False,json_dumps_params={'indent':2})
    return JsonResponse({'error':'Vacancy not found'})

def vacancies_of_company(request, company_id):
    company = Company.objects.get(pk= company_id)

    print(company.id)
    vacancies = []
    for vacancy in Vacancy.objects.all():
        vacancies.append(vacancy.to_json())  

    matching_vacancies = []

    for vacancy in vacancies:
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
