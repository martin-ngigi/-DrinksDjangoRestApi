# used for creating endpoints 
# endpoints are certain urls you can obtain data from

from dataclasses import dataclass
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response  import Response
from rest_framework import status

#can accept either get or post
#@api_view('GET', 'POST')
@api_view(['GET', 'POST'])
def drink_list(request):

    if request.method == 'GET':
        #1. get all drinks
        #2. serialize them
        #3. return json

        #1. get all drinks
        drinks = Drink.objects.all()

        #2. serialize them
        serializer = DrinkSerializer(drinks, many=True)

        #3. return json array
        #return JsonResponse(serializer.data, safe=False)
        
        #3. return json object
        return JsonResponse({'drinks':serializer.data})

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