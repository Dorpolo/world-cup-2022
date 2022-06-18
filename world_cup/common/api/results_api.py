from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Dict, Any


class StageType(Enum):
    GROUP = 'group_stage'
    KNOCKOUT = 'knockout'


class ResultAPIClient:
    def __init__(self, stage: StageType):
        self.stage = stage

    def get_live_matches(self) -> List[str]:
        pass

    def get_next_matches(self, n: int = None) -> List[str]:
        pass

    def get_prev_matches(self, n: int = None) -> List[str]:
        pass

    def get_match_results(self, game_ids: List[str]) -> Dict[str, Any]:
        pass

    def get_match_metadata(self, game_ids: List[str]) -> Dict[str, Dict[str, Any]]:
        pass
