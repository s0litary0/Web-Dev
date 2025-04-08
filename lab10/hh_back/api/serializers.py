from rest_framework import serializers
from .models import Company, Vacancy, Position


# class CompanySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=100)
#     description = serializers.CharField()
#     city = serializers.CharField(max_length=100)
#     address = serializers.CharField()

# class VacancySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=100)
#     description = serializers.CharField()
#     salary = serializers.FloatField()
#     company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
#     position = serializers.PrimaryKeyRelatedField(queryset=Position.objects.all())

# class PositionSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=100)

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('id', 'name')

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'city', 'address')

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'salary', 'company', 'position')