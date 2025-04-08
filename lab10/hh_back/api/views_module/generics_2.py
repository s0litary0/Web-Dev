from rest_framework import generics

from ..models import Company, Vacancy
from ..serializers import CompanySerializer, VacancySerializer

class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_url_kwarg = 'company_id'

class VacanciesList(generics.ListCreateAPIView):
    # queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    def get_queryset(self):
        company_id = self.kwargs['company_id']  # Get company_id from the URL
        return Vacancy.objects.filter(company_id=company_id)  # Filter vacancies for this company
