from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from .models import Companies
from rest_framework.views import status
from django.urls import reverse
from .serializers import CompaniesSerializer
# Create your tests here.

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_company(companyName="", companyAddress=""):
        if companyName!="" and companyAddress!="":
            Companies.objects.Create(companyName=companyName, companyAddress=companyAddress)

        def setUp(self):
        # add test data
            self.create_company("AkhilCompany", "banglore")
            self.create_company("AnkitCompany", "chandigarh")
            self.create_company("Akeys", "Patiala")

class getAllCompanies(BaseViewTest):

    def testGetAllCompanies(self):

 # hit the API endpoint
        response = self.client.get("all-companies")
        
        # fetch the data from db
        expected = Companies.objects.all()
        serialized = CompaniesSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


        

