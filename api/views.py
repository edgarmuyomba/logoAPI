from django.shortcuts import render
from rest_framework.response import Response
from .models import Logo, CATEGORIES
from .serializers import LogoSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse

@api_view(['GET'])
def company(request, company_name):
    comp_logo = Logo.objects.filter(company=company_name)
    data = LogoSerializer(comp_logo, many=True).data 
    return Response(data)

@api_view(['GET'])
def categories(request):
    categories = [cat[0] for cat in CATEGORIES]
    return JsonResponse(categories, safe=False)

@api_view(['GET'])
def category(request, cat_name):
    logos = Logo.objects.filter(category=cat_name)
    data = LogoSerializer(logos, many=True).data
    return Response(data)

@api_view(['GET'])
def random(request, num):
    logos = Logo.objects.order_by('?').all()[0:num]
    data = LogoSerializer(logos, many=True).data
    return Response(data)