from api.models import Company, Vacancy
from rest_framework import serializers


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    description = serializers.CharField()
    city = serializers.CharField(max_length=50)
    address = serializers.CharField()


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'name')