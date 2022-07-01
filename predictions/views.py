from django.http import HttpResponse
from django.shortcuts import render, redirect

from common.api.results_api import ResultAPIClient, StageType
from common.configs import ENV
from .forms import Top2PredictionForm, Top16PredictionForm, Top4PredictionForm, GroupStagePredictionForm, \
    Top8PredictionForm

from .utils.predictions_api import STAGE_MAPPER


def get_form(stage_type: StageType) -> type:
    if stage_type is StageType.GROUP:
        return GroupStagePredictionForm
    elif stage_type is StageType.KNOCKOUT_16:
        return Top16PredictionForm
    elif stage_type is StageType.KNOCKOUT_8:
        return Top8PredictionForm
    elif stage_type is StageType.KNOCKOUT_4:
        return Top4PredictionForm
    elif stage_type is StageType.KNOCKOUT_2:
        return Top2PredictionForm


class CRUDPrediction:
    def __init__(self, stage_type: StageType):
        self.data = ResultAPIClient(ENV).get_stage_matches(stage_type)
        self.context = {
            'data': self.data,
            'form_metadata': stage_type.round_names
        }
        self.stage_type = stage_type
        self.object = STAGE_MAPPER[stage_type]

    def create(self, request) -> HttpResponse:
        form = get_form(self.stage_type)

        if request.method == 'POST':
            form = get_form(self.stage_type)(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        return render(
            request=request,
            template_name='predictions/create_prediction.html',
            context=dict(**self.context, form=form)
        )

    def update(self, request, pk) -> HttpResponse:
        prediction = self.object.objects.get(id=pk)
        form = get_form(self.stage_type)(instance=prediction)
        if request.method == 'POST':
            form = get_form(self.stage_type)(request.POST, instance=prediction)
            if form.is_valid():
                form.save()
                return redirect('/')
        return render(
            request=request,
            template_name='predictions/create_prediction.html',
            context=dict(**self.context, form=form)
        )

