import os
from dataclasses import dataclass


from typing import List, Dict, Any, Union
from common.api.results_api import StageType, ResultAPIClient

from predictions.models import ExtraPrediction, GroupStagePrediction, Top16Prediction, Top8Prediction,\
    Top4Prediction, Top2Prediction
from league.models import League


STAGE_MAPPER: Dict[StageType, Any] = {
    StageType.GROUP: GroupStagePrediction,
    StageType.KNOCKOUT_16: Top16Prediction,
    StageType.KNOCKOUT_8: Top8Prediction,
    StageType.KNOCKOUT_4: Top4Prediction,
    StageType.KNOCKOUT_2: Top2Prediction,
}


class PredictionAPIClient:
    def __init__(self, stage_type: StageType):
        self.stage_type = stage_type
        self.stage_prediction = STAGE_MAPPER[stage_type]
        pass

    def get_user_leagues(self, user_id: str) -> List[Dict[str, Any]]:
        pass

    def get_stage_league_predictions(self, league_id: str = 1):
        data = League.objects.all()
        return {'policy_gs_90_min_score': k.policy_gs_90_min_score for k in data}

    def get_stage_user_predictions(self, user_id: str) -> List[Dict[str, Any]]:
        pass

    def get_match_league_predictions(self, league_id: str, match_id: str) -> List[Dict[str, Any]]:
        pass

    def get_match_user_predictions(self, user_id: str, match_id: str) -> List[Dict[str, Any]]:
        pass

