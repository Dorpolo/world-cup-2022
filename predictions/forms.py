from enum import Enum

from django.forms import ModelForm
from .models import GroupStagePrediction, Top16Prediction, Top8Prediction, Top4Prediction, Top2Prediction


class GroupStagePredictionForm(ModelForm):
    label = 'Group Stage'

    class Meta:
        model = GroupStagePrediction
        fields = '__all__'


class Top16PredictionForm(ModelForm):
    label = 'Top 16'

    class Meta:
        model = Top16Prediction
        fields = '__all__'


class Top8PredictionForm(ModelForm):
    label = 'Quarter Final'

    class Meta:
        model = Top8Prediction
        fields = '__all__'


class Top4PredictionForm(ModelForm):
    label = 'Semi Final'

    class Meta:
        model = Top4Prediction
        fields = '__all__'


class Top2PredictionForm(ModelForm):
    label = 'Final'

    class Meta:
        model = Top2Prediction
        fields = '__all__'
