import os
from enum import Enum

API_KEY = "bfa132288504de6860c8ae3259d21fa7"


class EnvType(Enum):
    PROD = '121'
    STG = '40'


ENV: EnvType = EnvType.STG
