from django.http import HttpResponse
from django.shortcuts import render

from common.api.results_api import ResultAPIClient
from common.api.teams_api import EnvType

env: EnvType = EnvType.PROD


def match_predictions(request) -> HttpResponse:
    results = ResultAPIClient(env)
    return render(
        request=request,
        template_name='predictions/predictions.html',
        context={'data': results.get_all_matches()}
    )


def single_match_prediction(request, pk) -> HttpResponse:
    return render(request, 'predictions/single_match_prediction.html')
