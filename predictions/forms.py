from django.forms import ModelForm
from .models import GroupStagePrediction, Top16Prediction, Top8Prediction, Top4Prediction, Top2Prediction


class GroupStagePredictionForm(ModelForm):
    class Meta:
        model = GroupStagePrediction
        fields = '__all__'