import os

from django.http import JsonResponse

pg: str = os.getenv('PG_PASS') if os.getenv('PG_PASS') else "key was not fount"


def ping(request):
    data = {'ping': pg}
    return JsonResponse(data)
