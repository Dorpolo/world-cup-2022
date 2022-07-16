from enum import Enum
from typing import List, Dict

from django.forms import ModelForm, widgets
from django import forms
from .models import GroupStagePrediction, Top16Prediction, Top8Prediction, Top4Prediction, Top2Prediction
from common.api.results_api import ResultAPIClient, StageType


def get_match_related_fields(match_id: str) -> List[str]:
    return [f"{match_id}_h", f"{match_id}_a", f"{match_id}_w"]


def get_stage_field(stage_type: StageType) -> List[str]:
    stage_matches: List[Dict[str, str]] = ResultAPIClient().get_stage_matches(stage_type)
    match_ids: List[str] = [match['match_id'] for match in stage_matches]
    match_fields: List[List[str]] = [get_match_related_fields(match_id) for match_id in match_ids]
    return [x for xs in match_fields for x in xs]


class GroupStagePredictionForm(ModelForm):
    label = 'Group Stage'

    class Meta:
        model = GroupStagePrediction
        fields: List[str] = get_stage_field(StageType.GROUP)
        widgets = {
            k: forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '-'}) if '_w' not in k
            else forms.Select(attrs={'class': 'form-select'}) for k in fields
        }

    def __init__(self, *args, **kwargs):
        super(GroupStagePredictionForm, self).__init__(*args, **kwargs)

        # for name, field in self.fields.items():
        #     field.widget.attrs.update({'class': 'input'})


class Top16PredictionForm(ModelForm):
    label = 'Top 16'

    class Meta:
        model = Top16Prediction
        fields: List[str] = get_stage_field(StageType.KNOCKOUT_16)
        widgets = {
            k: forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '-'}) if '_w' not in k
            else forms.Select(attrs={'class': 'form-select'}) for k in fields
        }

    def __init__(self, *args, **kwargs):
        super(Top16PredictionForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class Top8PredictionForm(ModelForm):
    label = 'Quarter Final'

    class Meta:
        model = Top8Prediction
        fields: List[str] = get_stage_field(StageType.KNOCKOUT_8)
        widgets = {
            k: forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '-'}) if '_w' not in k
            else forms.Select(attrs={'class': 'form-select'}) for k in fields
        }

    def __init__(self, *args, **kwargs):
        super(Top8PredictionForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class Top4PredictionForm(ModelForm):
    label = 'Semi Final'

    class Meta:
        model = Top4Prediction
        fields: List[str] = get_stage_field(StageType.KNOCKOUT_4)
        widgets = {
            k: forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '-'}) if '_w' not in k
            else forms.Select(attrs={'class': 'form-select'}) for k in fields
        }

    def __init__(self, *args, **kwargs):
        super(Top4PredictionForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class Top2PredictionForm(ModelForm):
    label = 'Final'

    class Meta:
        model = Top2Prediction
        fields: List[str] = get_stage_field(StageType.KNOCKOUT_2)
        widgets = {
            k: forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '-'}) if '_w' not in k
            else forms.Select(attrs={'class': 'form-select'}) for k in fields
        }

    def __init__(self, *args, **kwargs):
        super(Top2PredictionForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
