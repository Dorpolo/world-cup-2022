import os

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render


def view_nav_bar(request) -> HttpResponse:
    return render(
        request=request,
        template_name='base.html',
    )
