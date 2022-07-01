from django.http import HttpResponse
from django.shortcuts import render

from common.api.results_api import ResultAPIClient, StageType
from common.configs import ENV
from predictions.utils.predictions_api import PredictionAPIClient


def league(request) -> HttpResponse:
    predictions = PredictionAPIClient(StageType.GROUP)
    results = ResultAPIClient(ENV)
    return render(
        request=request,
        template_name='league/league.html',
        context={'data': predictions.get_stage_league_predictions()}
    )


def single_league(request, pk) -> HttpResponse:
    return render(request, 'predictions/single_match_prediction.html')
