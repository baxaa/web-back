from django.urls import path

from api import views


urlpatterns = [
    path('companies', views.company_list),
    path('companies/<int:company_id>', views.Company_detail),
    path('companies/<int:company_id>/vacancies', views.vacancies_of_company),
    path('vacancies', views.VacancyAPIListView.as_view()),
    path('vacancies/<int:vacancy_id>', views.Vacancy_detail),
]