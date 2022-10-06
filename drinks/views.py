# used for creating endpoints 
# endpoints are certain urls you can obtain data from

from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

def drink_list(request):
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
    return JsonResponse({'drinks':serializer.data}, safe=False)