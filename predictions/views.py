from django.http import HttpResponse
from django.shortcuts import render

from common.api.results_api import ResultAPIClient
from common.configs import ENV

from .forms import GroupStagePredictionForm


def get_match_context():
    data = ResultAPIClient(ENV).get_all_matches()
    match_context = []
    for v in data:
        match_context.append([f"{v['match_id']}_h", f"{v['match_id']}_a", f"{v['match_id']}_w"])
    return {'data': data, 'match_context': match_context}


def group_stage_prediction(request) -> HttpResponse:
    context = {
        **get_match_context(),
        'form': GroupStagePredictionForm()
    }
    return render(
        request=request,
        template_name='predictions/gs_prediction.html',
        context=context
    )


def predictions(request) -> HttpResponse:
    results = ResultAPIClient(ENV)
    return render(
        request=request,
        template_name='predictions/predictions.html',
        context={'data': results.get_all_matches()}
    )


def single_match_prediction(request, pk) -> HttpResponse:
    return render(request, 'predictions/single_match_prediction.html')
