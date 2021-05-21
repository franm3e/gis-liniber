from django.http import JsonResponse
from webliniber.models import Animal
from django.core import serializers


def get_animals(request):
    return JsonResponse(serializers.serialize("json", Animal.objects.all()), safe=False, status=200) \
        if (request.is_ajax and request.method == "GET") \
        else JsonResponse({}, status=400)
