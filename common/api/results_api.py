import os
from dataclasses import dataclass

import requests

from enum import Enum
from typing import List, Dict, Any, Union

from pprint import pprint
import pandas as pd

from common.configs import ENV, API_KEY

os.environ['API_KEY'] = API_KEY


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

    def get_data(self):
        return self.__dict__


class EnvType(Enum):
    PROD = '121'
    STG = '40'


class StageType(Enum):
    GROUP = ('1st Round', '2nd Round', '3rd Round', )
    KNOCKOUT_16 = ('1/8 Final', )
    KNOCKOUT_8 = ('1/4 Final', )
    KNOCKOUT_4 = ('1/2 Final', )
    KNOCKOUT_2 = ('Final', )


class ResultAPIClient:
    def __init__(
        self,
        env: EnvType = EnvType.PROD
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

    def get_match(self, match_id: str) -> Dict[str, Any]:
        data: List[Dict[str, Any]] = self.get_all_matches()
        accepted_ids: List[str] = [item['match_id'] for item in data]
        assert match_id in accepted_ids, "The provided match id is not exists"
        return [item for item in data if item['match_id'] == match_id][0]

    def get_all_matches_df(self) -> pd.DataFrame:
        df = pd.DataFrame(self.get_all_matches())
        df['date'] = pd.to_datetime(df['match_date'])
        return df

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
        )

    def get_live_matches(self) -> Dict[str, Any]:
        df: pd.DataFrame = self.get_all_matches_df()
        live_df = df.loc[df.match_status == '0']
        return live_df.to_dict('index')

    def get_next_matches(self) -> List[str]:
        df: pd.DataFrame = self.get_all_matches_df()
        print(df["date"].argmin())
        return df.iloc[df["date"].argmax()].to_dict()

    def get_prev_matches(self, n: int = None) -> List[str]:
        pass

    def get_stage_matches(self, stage_type: StageType) -> List[Dict[str, Any]]:
        return [{
            'stage': item['stage'],
            'index': item['index'],
            'match_id': item['match_id'],
            'home': item['home_team_name'],
            'away': item['away_team_name']
        } for item in self.get_all_matches() if item['stage'] in stage_type.value]

    def get_all_data(self) -> Dict[str, Any]:
        url = f'{self.api_prefix}/matches/?season_id={self.season}&apikey={self.api_key}'
        return self.format_request(url)


# if __name__ == '__main__':
#     results = ResultAPIClient(ENV)
#     data = results.get_all_matches()
#
#     from pprint import pprint
#
#     pprint(results.get_stage_matches(StageType.GROUP))
#     pprint(data['calendar']['matchdays'])
#     for item in data['calendar']['matchdays']:
#         stage = item['stage']
