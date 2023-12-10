from enum import Enum

class ThrowDiceOrStop(Enum):
    Throw = 1
    Stop = 2


class MapChoises(Enum):
    Generated = 1
    Load = 2
    Custom = 3
    Default = 4