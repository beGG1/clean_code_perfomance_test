from typing import Optional

from src.internal.filters.filters import apply_filters
import numpy as np

def filter_ts_handler(ts: np.ndarray, filters: Optional[dict]):
    return apply_filters(ts, filters)