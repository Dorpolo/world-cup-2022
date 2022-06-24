import os
from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Dict, Any, Union

os.environ['API_KEY'] = "bfa132288504de6860c8ae3259d21fa7"


class EnvType(Enum):
    PROD = '40'
    STG = '40'

data = [
    {
     'awayParticipant': {
        'logo': 'https://api.statorium.com/media/bearleague/bl15773721822574.png',
        'participantID': '385',
        'participantName': 'Netherlands',
        'score': '0'
    },
    'group': {
        'groupID': '163',
        'groupName': 'Group A'
    },
      'homeParticipant': {
          'logo': 'https://api.statorium.com/media/bearleague/bl1632402538827.png',
          'participantID': '1066',
          'participantName': 'Senegal',
          'score': '0'
      },
      'matchDate': '2022-11-21',
      'matchID': '37637',
      'matchStatus': {'statusID': '0'},
      'matchTime': '10:00',
  'matchVenue': {'venueID': '1168'}
}]


if __name__ == '__main__':
    op = {'hey': k for k, v in data[0].items()}
    from pprint import pprint
    pprint(op)