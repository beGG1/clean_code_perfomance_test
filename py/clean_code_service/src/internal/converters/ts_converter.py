# Standard Library
from typing import List, Tuple, Union

# Third Party Library
import numpy as np


def ts2numpy(ts: List[Tuple]) -> np.ndarray:
    return np.array(ts)


def ts2dates(ts: Union[List[Tuple], np.ndarray]) -> np.ndarray:
    return np.array(ts)[:, 0]


def ts2vals(ts: Union[List[Tuple], np.ndarray]) -> np.ndarray:
    return np.array(ts)[:, -1]
