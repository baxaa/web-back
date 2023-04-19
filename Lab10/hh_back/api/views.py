from rest_framework.views import APIView
import json
from django.http.response import JsonResponse
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



class VacancyAPIListView(APIView):        
    def Vacancy_list(self, request):
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
