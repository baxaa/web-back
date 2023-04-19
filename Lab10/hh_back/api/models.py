from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=10000)
    city = models.CharField(max_length=255, default='')
    address = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def to_json(self):
        return {
            'id' : self.id,
            'name': self.name,
            'description' : self.description,
            'city' : self.city,
            'address' : self.address
        }

class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=10000)
    salary = models.FloatField(default=0)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,default = 5)

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def to_json(self):
        return {
            'id' : self.id,
            'name': self.name,
            'description':self.description,
            'salary' : self.salary,
            'company' : self.company.id
        }


