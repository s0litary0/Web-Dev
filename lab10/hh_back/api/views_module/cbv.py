from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
import rest_framework.status as status

from ..models import Company
from ..serializers import CompanySerializer


class CompanyListApiView(APIView):
    def get(self, request: Request) -> Response:
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyDetailApiView(APIView):
    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request: Request, company_id) -> Response:
        company = self.get_object(company_id)
        serializer = CompanySerializer(company)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, company_id) -> Response:
        company = self.get_object(company_id)
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, company_id) -> Response:
        company = self.get_object(company_id)
        company.delete()
        return Response({"deleted": True},status=status.HTTP_200_OK)