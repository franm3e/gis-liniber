from django.http import JsonResponse
from webliniber.models import AnimalView
from django.core import serializers


def get_animals(request):
    return JsonResponse(serializers.serialize("json", AnimalView.objects.all()), safe=False, status=200) \
        if (request.is_ajax and request.method == "GET") \
        else JsonResponse({}, status=400)
