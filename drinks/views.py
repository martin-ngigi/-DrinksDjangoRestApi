# used for creating endpoints 
# endpoints are certain urls you can obtain data from

#   YOUTUBE LINK
#https://www.youtube.com/watch?v=i5JykvxUk_A&t=44s

from dataclasses import dataclass
from django.http import JsonResponse
from django.urls import is_valid_path
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response  import Response
from rest_framework import status

# Post -> insert new record(Create)
# Put -> update data

#can accept either get or post
#@api_view('GET', 'POST')
@api_view(['GET', 'POST'])
def drink_list(request, format=None):

    if request.method == 'GET':
        #1. get all drinks
        #2. serialize them
        #3. return json

        # #1. get all drinks
        drinks = Drink.objects.all()

        # #2. serialize them
        # serializer = DrinkSerializer(drinks, many=True)

        # #3. return json array
        # #return JsonResponse(serializer.data, safe=False)
        
        # #3. return json object
        # return JsonResponse({'drinks':serializer.data})

        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data)


    if request.method == 'POST':
        #1.get python data
        #2. decerialize it (convert from json to python)
        #3. return python data

        #1. get python data from request
        serializer = DrinkSerializer(data = request.data)
        #validate data
        if serializer.is_valid():
            serializer.save()#if data is valid, save it
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        #2. decerialize it (convert from json to python)
        #3. return python data

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None): #id is frpm urls.py
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        # if serializer is_valid save data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        #else show error message
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
