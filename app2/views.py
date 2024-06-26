from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *


# //********************** CRUD DRINK ***********************//
@api_view(['GET', 'POST'])
def drink_list(request, format=None):
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return JsonResponse({'data': serializer.data}, safe=False)
    if request.method == 'POST':
        drink_serializer = DrinkSerializer(data=request.data, )
        if drink_serializer.is_valid():
            drink_serializer.save()
            return JsonResponse(drink_serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):
    if request.method == 'GET':
        drink = Drink.objects.get(pk=id)
        serializer = DrinkSerializer(drink)
        return JsonResponse({'data': serializer.data}, safe=False)
    return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        drink_serializer = DrinkSerializer(data=request.data)
        if drink_serializer.is_valid():
            drink_serializer.save()
            return JsonResponse(drink_serializer.data, status=status.HTTP_200_OK)
        return Response(drink_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        drink_serializer = DrinkSerializer(data=request.data)
        if drink_serializer.is_valid():
            drink_serializer.save()
            return JsonResponse(drink_serializer.data, status=status.HTTP_200_OK)
        return Response(drink_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ********************************** GESTIONAIRE **********************************
@api_view(['GET', 'POST'])
def gestionaires_list(request, format=None):
    if request.method == 'GET':
        gestionaires = Gestionaire.objects.all()
        serializer = GestionaireSerializer(gestionaires, many=True)
        return JsonResponse({'data': serializer.data}, safe=False)
    if request.method == 'POST':
        gestionaire_serializer = GestionaireSerializer(data=request.data, )
        if gestionaire_serializer.is_valid():
            gestionaire_serializer.save()
            return JsonResponse(gestionaire_serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def gestionaires_detail(request, id, format=None):
    if request.method == 'GET':
        gestionaire = Gestionaire.objects.get(pk=id)
        serializer = GestionaireSerializer(gestionaire)
        return JsonResponse({'data': serializer.data}, safe=False)
    return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        gestionaire_serializer = GestionaireSerializer(data=request.data)
        if gestionaire_serializer.is_valid():
            gestionaire_serializer.save()
            return JsonResponse(gestionaire_serializer.data, status=status.HTTP_200_OK)
        return Response(gestionaire_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        gestionaire_serializer = GestionaireSerializer(data=request.data)
        if gestionaire_serializer.is_valid():
            gestionaire_serializer.save()
            return JsonResponse(gestionaire_serializer.data, status=status.HTTP_200_OK)
        return Response(gestionaire_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
