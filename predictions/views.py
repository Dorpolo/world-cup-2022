from typing import List, Dict

from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from common.api.results_api import ResultAPIClient, StageType
from common.configs import ENV
from users.models import Profile
from .forms import Top2PredictionForm, Top16PredictionForm, Top4PredictionForm, GroupStagePredictionForm, \
    Top8PredictionForm, get_match_related_fields

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
            'form_metadata': stage_type.round_names,
            'form_label': get_form(stage_type)().label
        }
        self.stage_type = stage_type
        self.object = STAGE_MAPPER[stage_type]

    def create(self, request) -> HttpResponse:
        form = get_form(self.stage_type)

        if request.method == 'POST':
            user = request.user
            if user.is_authenticated:

                user = User.objects.get(pk=request.user.id)
                profile = Profile.objects.get(user=user)
                form = get_form(self.stage_type)(request.POST)
                if form.is_valid():
                    filled_form = form.save(commit=False)
                    filled_form.user_id = request.user.id
                    filled_form.save()
                    return redirect('/')
                else:
                    print(form)
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


from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from . import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Submit, Div


class DetailView(generic.DetailView):
    template_name = 'predictions/detail_page.html'
    model = models.Top2Prediction


def get_stage_field(stage_type: StageType) -> List[str]:
    stage_matches: List[Dict[str, str]] = ResultAPIClient().get_stage_matches(stage_type)
    match_ids: List[str] = [match['match_id'] for match in stage_matches]
    match_fields: List[List[str]] = [get_match_related_fields(match_id) for match_id in match_ids]
    return [x for xs in match_fields for x in xs]


class Row(Div):
    css_class = "row"


class PredictForm(ModelForm):
    class Meta:
        # model = models.Top2Prediction
        # fields: List[str] = get_stage_field(StageType.KNOCKOUT_2) + ['user']
        model = models.GroupStagePrediction
        fields: List[str] = get_stage_field(StageType.GROUP) + ['user']


    @property
    def helper(self):
        data = ResultAPIClient(ENV).get_stage_matches(StageType.GROUP)
        helper = FormHelper()
        helper.layout = Layout(
            HTML("<h1>Submit Your Predictions!</h1>"),
        )
        for match in data:
            helper.layout.append(
                Row(
                    Field(list(match['form_fields'].keys())[0], wrapper_class='col-sm-2'),
                    Field(list(match['form_fields'].keys())[1], wrapper_class='col-sm-10'),
                    Field(list(match['form_fields'].keys())[2], wrapper_class='col-sm-10')
                ),
            )
        helper.layout.append(HTML("<hr>"))
        helper.layout.append(Submit('submit', 'Submit your predictions', css_class='btn-success'))
        helper.field_class = 'col-9'
        helper.label_class = 'col-3'
        return helper


class CreateView(SuccessMessageMixin, generic.CreateView):
    template_name = 'predictions/create.html'
    success_message = 'Your Predictions submitted successfully'
    form_class = PredictForm
    # if request.method == 'POST':
    #     user = request.user
    #     if user.is_authenticated:
    #         user = User.objects.get(pk=request.user.id)
    #
    #     user = User.objects.get(pk=request.user.id)
    #     profile = Profile.objects.get(user=user)
    #     form = get_form(self.stage_type)(request.POST)
    #     if form.is_valid():
    #         filled_form = form.save(commit=False)
    #         filled_form.user_id = request.user.id
    #         filled_form.save()
    #         return redirect('/')
    # GET:
    #   Form
    # POST:
    #   csrf
    #   validate
    #   save
    #   redirect to a success page (Details page)
    #       read the get_absolute_url from the object
