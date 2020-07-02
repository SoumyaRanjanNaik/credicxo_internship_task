from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from banks.models import Bank
from banks.serializers import BankSerializer

# Create your views here.
@api_view(
    ["GET",]
)
def get_branch_details(request):
    """
    REQUEST METHOD : 
        - GET
    PARAMETERS REQUIRED : 
        - ifsc
    SUCCESS :
        - Details of the bank that has the same ifsc code is returned
    FAILURE :
        - nothing is sent in response only HTTP 404 is sent
    """
    try:
        bank = Bank.objects.get(ifsc=request.query_params.get("ifsc"))
        ser = BankSerializer(bank)
        return Response(ser.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(
    ["GET",]
)
def get_branches_in_city(request):
    """
    REQUEST METHOD : 
        - GET
    PARAMETERS REQUIRED : 
        - bank_name
        - city
    SUCCESS :
        - a list of banks with same name and same city
    FAILURE :
        - nothing is sent in response only HTTP 404 is sent
    """
    try:
        bank = Bank.objects.filter(
            bank_name=request.query_params.get("bank_name"),
            city=request.query_params.get("city"),
        )
        ser = BankSerializer(bank, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
