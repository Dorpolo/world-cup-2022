import uuid
from typing import List, Any, Dict, Tuple

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from common.api.results_api import ResultAPIClient, StageType
from common.configs import ENV

# initiate API class instance
results: ResultAPIClient = ResultAPIClient(ENV)


def get_winner_choice(home_team: str, away_team: str, is_group_stage: bool = False) -> Tuple:
    if is_group_stage:
        return (
            (home_team, home_team),
            (away_team, away_team),
            ('draw', 'draw')
        )
    else:
        return (
            (home_team, home_team),
            (away_team, away_team),
        )


# Group Stage Model
class ExtraPrediction(models.Model):
    PLAYERS = (('polo', 'Polo'), )
    TEAMS = (('mta', 'MTA'), )
    top_scorer = models.CharField(choices=PLAYERS, max_length=50)
    top_assists = models.CharField(choices=PLAYERS, max_length=50)
    winning_team = models.CharField(choices=TEAMS, max_length=50)


class BasePrediction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# Group Stage Model
class GroupStagePrediction(BasePrediction):
    pass


group_stage_data: List[Dict[str, Any]] = results.get_stage_matches(StageType.GROUP)
for record in group_stage_data:
    winner_choices: Tuple[Tuple[str, str]] = get_winner_choice(record['home'], record['away'], True)
    GroupStagePrediction.add_to_class(f"{record['match_id']}_h", models.IntegerField())
    GroupStagePrediction.add_to_class(f"{record['match_id']}_a", models.IntegerField())
    GroupStagePrediction.add_to_class(f"{record['match_id']}_w", models.CharField(choices=winner_choices, max_length=50))


# 1/8 Final Model
class Top16Prediction(BasePrediction):
    pass


top_16_data: List[Dict[str, Any]] = results.get_stage_matches(StageType.KNOCKOUT_16)
for record in top_16_data:
    winner_choices: Tuple[Tuple[str, str]] = get_winner_choice(record['home'], record['away'])
    Top16Prediction.add_to_class(f"{record['match_id']}_h", models.IntegerField())
    Top16Prediction.add_to_class(f"{record['match_id']}_a", models.IntegerField())
    Top16Prediction.add_to_class(f"{record['match_id']}_w", models.CharField(choices=winner_choices, max_length=50))


# 1/8 Final Model
class Top8Prediction(BasePrediction):
    pass


top_8_data: List[Dict[str, Any]] = results.get_stage_matches(StageType.KNOCKOUT_8)
for record in top_8_data:
    winner_choices: Tuple[Tuple[str, str]] = get_winner_choice(record['home'], record['away'])
    Top8Prediction.add_to_class(f"{record['match_id']}_h", models.IntegerField())
    Top8Prediction.add_to_class(f"{record['match_id']}_a", models.IntegerField())
    Top8Prediction.add_to_class(f"{record['match_id']}_w", models.CharField(choices=winner_choices, max_length=50))


# 1/2 Final Model
class Top4Prediction(BasePrediction):
    pass


top_4_data: List[Dict[str, Any]] = results.get_stage_matches(StageType.KNOCKOUT_4)
for record in top_4_data:
    winner_choices: Tuple[Tuple[str, str]] = get_winner_choice(record['home'], record['away'])
    Top4Prediction.add_to_class(f"{record['match_id']}_h", models.IntegerField())
    Top4Prediction.add_to_class(f"{record['match_id']}_a", models.IntegerField())
    Top4Prediction.add_to_class(f"{record['match_id']}_w", models.CharField(choices=winner_choices, max_length=50))


# Final Model
class Top2Prediction(BasePrediction):
    pass


top_2_data: List[Dict[str, Any]] = results.get_stage_matches(StageType.KNOCKOUT_2)
for record in top_2_data:
    winner_choices: Tuple[Tuple[str, str]] = get_winner_choice(record['home'], record['away'])
    Top2Prediction.add_to_class(f"{record['match_id']}_h", models.IntegerField())
    Top2Prediction.add_to_class(f"{record['match_id']}_a", models.IntegerField())
    Top2Prediction.add_to_class(f"{record['match_id']}_w", models.CharField(choices=winner_choices, max_length=50))
