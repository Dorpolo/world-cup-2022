from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def profiles(request) -> HttpResponse:
    return render(
        request=request,
        template_name='users/profiles.html',
    )
