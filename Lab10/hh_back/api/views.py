# from django.shortcuts import render
# import json
# from django.http.response import HttpResponse, JsonResponse
# from datetime import datetime, timedelta
# import requests

# from api.models import Vacancy, Vacancy



# def list_of_companies(request):
#     # if request.method == 'GET':
#     companies = Company.objects.all()
#     companies_json = [p.to_json() for p in companies]
#     return JsonResponse(companies_json,safe=False)


# def company_detail(request, company_id):
#     try:
#         company = Company.objects.get(id = company_id)
#     except Company.DoesNotExist as e:
#         return JsonResponse({'error': str(e)}, status=400)
#     # if request.method == 'GET':
#     return JsonResponse(company.to_json(),safe=False)


# def list_of_vacancies(request):
#     # if request.method == 'GET':
#     vacancies = Vacancy.objects.all()
#     vacancies_json = [p.to_json() for p in vacancies]
#     return JsonResponse(vacancies_json,safe=False)
        

# def vacancy_detail(request,vacancy_id):
#     try:
#         vacancy = Vacancy.objects.get(id = vacancy_id)
#     except Vacancy.DoesNotExist as e:
#         return JsonResponse({'error': str(e)}, status=400)
#     # if request.method == 'GET':
#     return JsonResponse(vacancy.to_json(),safe=False)

# def vacancies_of_company(request, company_id):
#     vacancies = Vacancy.objects.all()
#     vacancies_json = [p.to_json() for p in vacancies]

#     company = Company.objects.get(pk= company_id)
#     matching_vacancies = []

#     for vacancy in vacancies_json:
#         if vacancy['company'] == company.id:
#             matching_vacancies.append(vacancy)

#     if len(matching_vacancies) != 0:
#         return JsonResponse(matching_vacancies,safe=False,json_dumps_params={'indent':2})
#     return JsonResponse({'error':'Vacancies not found'})

# def top_ten_vacancies(request):
#     vacancies = []
#     for vacancy in Vacancy.objects.all():
#         vacancies.append(vacancy.to_json())
#     sorted_array = sorted(vacancies, key = lambda x : x['salary'], reverse= True)
#     # vacancies.reverse()
#     if(sorted_array.count != 0):
#         return JsonResponse(sorted_array[0:11],safe=False,json_dumps_params={'indent':2})
#     return JsonResponse({'error':'Error404'})


# import json
# from django.views.decorators.csrf import csrf_exempt
# from django.http.response import JsonResponse
# from api.models import Company, Vacancy


# # CRUD - CRATE, READ, UPDATE, DELETE

# @csrf_exempt
# def company_list(request):
#     if request.method == 'GET':
#         companies = Company.objects.all()
#         companies_json = [p.to_json() for p in companies]
#         return JsonResponse(companies_json,safe=False)
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         print(data)
#         company_name = data.get('Name', '')
#         company = Company.objects.create(name=company_name)
#         return JsonResponse(company.to_json())


# @csrf_exempt
# def Company_detail(request, company_id):
#     try:
#         company = Company.objects.get(id=company_id)
#     except Company.DoesNotExist as e:
#         return JsonResponse({'error': str(e)}, status=400)

#     if request.method == 'GET':
#         return JsonResponse(company.to_json())
#     elif request.method == 'PUT':
#         data = json.loads(request.body)
#         new_company_name = data.get('name', company.name)
#         # desc = data.get('desc', Company.desc)
#         company.name = new_company_name
#         company.save()
#         return JsonResponse(company.to_json())
#     elif request.method == 'DELETE':
#         company.delete()
#         return JsonResponse({'deleted': True})

# @csrf_exempt
# def Vacancy_list(request):
#     if request.method == 'GET':
#         vacancies = Vacancy.objects.all()
#         vacancies_json = [p.to_json() for p in vacancies]
#         return JsonResponse(vacancies_json, safe=False)
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         print(data)
#         vacancy_name = data.get('name', '')
#         # company_id = data.get('company', '')
#         vacancy = Vacancy.objects.create(name=vacancy_name)
#         return JsonResponse(vacancy.to_json())

# @csrf_exempt
# def Vacancy_detail(request, Vacancy_id):
#     try:
#         vacancy = Vacancy.objects.get(id=Vacancy_id)
#     except Vacancy.DoesNotExist as e:
#         return JsonResponse({'error': str(e)}, status=400)

#     if request.method == 'GET':
#         return JsonResponse(vacancy.to_json())
#     elif request.method == 'PUT':
#         data = json.loads(request.body)
#         new_vacancy_name = data.get('name', vacancy.name)
#         # desc = data.get('desc', Vacancy.desc)
#         vacancy.name = new_vacancy_name
#         vacancy.save()
#         return JsonResponse(vacancy.to_json())
#     elif request.method == 'DELETE':
#         vacancy.delete()
#         return JsonResponse({'deleted': True})



from django.shortcuts import render
import json
from django.http.response import HttpResponse, JsonResponse
from datetime import datetime, timedelta
import requests
from api.serializers import CompanySerializer, VacancySerializer

from api.models import Company, Vacancy


def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies = [p.to_json() for p in companies]
        serializer = CompanySerializer(companies,many = True)
        return JsonResponse(serializer.data,safe = False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = CompanySerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)


def Company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = CompanySerializer(instance=company, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'deleted': True})




def Vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        vacancies = [p.to_json() for p in vacancies]
        serializer = VacancySerializer(vacancies,many = True)
        return JsonResponse(serializer.data,safe = False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = VacancySerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)


def Vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    if request.method == 'GET':
        serializer = VacancySerializer(vacancy)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = VacancySerializer(instance=vacancy, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({'deleted': True})


def vacancies_of_company(request,company_id):
    vacancies = []
    for vacancy in Vacancy.objects.all():
        vacancies.append(vacancy.to_json())

    company = Company.objects.get(pk = company_id)

    matching_vacancies = []
    for vacancy in vacancies:
        if vacancy['company'] == company.id:
            matching_vacancies.append(vacancy)

    if matching_vacancies.count != 0:
        return JsonResponse(matching_vacancies,safe=False,json_dumps_params={'indent':2})
    return JsonResponse({'error':'Vacancies not found'})

def top_ten_vacancies(request):
    vacancies = []
    for vacancy in Vacancy.objects.all():
        vacancies.append(vacancy.to_json())
    vacancies = sorted(vacancies,key = lambda x : x['salary'],reverse=True)
    if(vacancies.count != 0):
        return JsonResponse(vacancies[0:11],safe=False,json_dumps_params={'indent':2})
    return JsonResponse({'error':'Error404'})
