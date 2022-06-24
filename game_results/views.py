from django.http import HttpResponse
from django.shortcuts import render

from common.api.results_api import ResultAPIClient
from common.api.teams_api import EnvType

env: EnvType = EnvType.PROD


def game_results(request) -> HttpResponse:
    results = ResultAPIClient(env)
    return render(
        request=request,
        template_name='game_results/game_results.html',
        context={'data': results.get_all_matches()}
    )


def game_result(request, pk) -> HttpResponse:
    return render(request, 'game_results/game_result.html')
