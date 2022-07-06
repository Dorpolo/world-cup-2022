import os
from dataclasses import dataclass

import requests

from enum import Enum
from typing import List, Dict, Any, Union

from pprint import pprint
# import pandas as pd

from common.configs import API_KEY, ENV, EnvType


os.environ['API_KEY'] = API_KEY


class StageType(Enum):
    GROUP = ('1st Round', '2nd Round', '3rd Round', ), 1
    KNOCKOUT_16 = ('1/8 Final', ), 2
    KNOCKOUT_8 = ('1/4 Final', ), 3
    KNOCKOUT_4 = ('1/2 Final', ), 4
    KNOCKOUT_2 = ('Final', ), 5

    def __init__(self, round_names, stage_id):
        self.round_names = round_names
        self.stage_id = stage_id


@dataclass
class MatchMetaData:
    match_id: str
    match_status: str
    match_date: str
    match_time: str
    group_id: str
    group_name: str
    home_team_id: str
    home_team_name: str
    home_team_logo: str
    home_team_score: str
    away_team_id: str
    away_team_name: str
    away_team_logo: str
    away_team_score: str
    form_fields: List[str] = None

    def get_data(self):
        return self.__dict__


class ResultAPIClient:
    def __init__(
        self,
        env: EnvType = ENV
    ):
        self.api_key = os.getenv('API_KEY')
        self.season = env.value
        self.api_prefix = 'https://api.statorium.com/api/v1'

    @staticmethod
    def format_request(url) -> Union[Dict[str, Any], None]:
        return requests.get(url=url).json()

    def get_matches_metadata(self) -> Dict[str, Dict[str, Any]]:
        url = f'{self.api_prefix}/matches/?season_id={self.season}&apikey={self.api_key}'
        data = self.format_request(url)
        record = {
            item['matchdayName']: item['matches'] for item in data['calendar'].get('matchdays')
        }
        return record

    def get_all_matches(self) -> List[Dict[str, str]]:
        data: Dict[str, Dict[str, Any]] = self.get_matches_metadata()
        res = []
        for k, v in data.items():
            res += [{
                'index': i,
                'stage': k,
                **self.get_valid_record(item).get_data(),
            } for i, item in enumerate(v)]
        return res

    def get_stage_matches(self, stage_type: StageType) -> List[Dict[str, str]]:
        data = self.get_all_matches()
        return [item for item in data if item['stage'] in stage_type.round_names]

    def get_match(self, match_id: str) -> Dict[str, Any]:
        data: List[Dict[str, Any]] = self.get_all_matches()
        accepted_ids: List[str] = [item['match_id'] for item in data]
        assert match_id in accepted_ids, "The provided match id is not exists"
        return [item for item in data if item['match_id'] == match_id][0]

    @staticmethod
    def get_valid_record(record: Dict[str, Any]) -> MatchMetaData:
        return MatchMetaData(
            match_id=record['matchID'],
            match_status=record['matchStatus']['statusID'],
            match_date=record['matchDate'],
            match_time=record['matchTime'],
            group_id=record['group']['groupID'],
            group_name=record['group']['groupName'],
            home_team_id=record['homeParticipant']['participantID'],
            home_team_name=record['homeParticipant']['participantName'],
            home_team_logo=record['homeParticipant']['logo'],
            home_team_score=record['homeParticipant']['score'],
            away_team_id=record['awayParticipant']['participantID'],
            away_team_name=record['awayParticipant']['participantName'],
            away_team_logo=record['awayParticipant']['logo'],
            away_team_score=record['awayParticipant']['score'],
            form_fields=ResultAPIClient.get_form_fields(record)
        )

    @staticmethod
    def get_form_fields(record: Dict[str, Any]) -> List[str]:
        match_id: str = record['matchID']
        return [f"{match_id}_{field}" for field in ['h', 'a', 'w']]

    def get_prev_matches(self, n: int = None) -> List[str]:
        pass

    def fetch_stage_matches(self, stage_type: StageType) -> List[Dict[str, Any]]:
        return [{
            'stage': item['stage'],
            'index': item['index'],
            'match_id': item['match_id'],
            'home': item['home_team_name'],
            'away': item['away_team_name']
        } for item in self.get_all_matches() if item['stage'] in stage_type.round_names]

    def get_all_data(self) -> Dict[str, Any]:
        url = f'{self.api_prefix}/matches/?season_id={self.season}&apikey={self.api_key}'
        return self.format_request(url)


if __name__ == '__main__':
    def get_match_related_fields(match_id: str) -> List[str]:
        return [f"{match_id}_h", f"{match_id}_a", f"{match_id}_w"]


    def get_stage_field(stage_type: StageType) -> List[str]:
        stage_matches: List[Dict[str, str]] = ResultAPIClient().get_stage_matches(stage_type)
        print(stage_matches)
        match_ids: List[str] = [match['match_id'] for match in stage_matches]
        match_fields: List[List[str]] = [get_match_related_fields(match_id) for match_id in match_ids]
        return [x for xs in match_fields for x in xs]


    print(ResultAPIClient().get_stage_matches(StageType.GROUP))


