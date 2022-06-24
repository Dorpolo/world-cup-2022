from django.http import HttpResponse
from django.shortcuts import render

from common.api.results_api import ResultAPIClient
from common.configs import ENV


def predictions(request) -> HttpResponse:
    results = ResultAPIClient(ENV)
    return render(
        request=request,
        template_name='predictions/predictions.html',
        context={'data': results.get_all_matches()}
    )


def single_match_prediction(request, pk) -> HttpResponse:
    return render(request, 'predictions/single_match_prediction.html')
