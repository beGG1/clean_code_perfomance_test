# Standard Library
from typing import Dict, List, Optional, Set

# Third Party Library
import numpy as np
from loguru import logger
from src.internal.filters import ts_filters


def init_filter(filter_name: str) -> ts_filters.AbstractFilter:
    return getattr(ts_filters, filter_name)()


def get_all_filters() -> Set:
    return {class_instance.__name__ for class_instance in ts_filters.AbstractFilter.__subclasses__()}


def apply_filters(ts: np.ndarray, filters: Optional[List[Dict]] = None) -> np.ndarray:

    if not filters:
        return np.array(ts)

    all_possible_filters = get_all_filters()

    for flt in filters:
        if flt.ts_algorithm in all_possible_filters:
            if flt.input_kwargs:
                ts = init_filter(flt.ts_algorithm).apply_filter(ts, **flt.input_kwargs)
            else:
                ts = init_filter(flt.ts_algorithm).apply_filter(ts)
        else:
            logger.critical(f'FILTER | Filter {flt} does not exist')

    return np.array(ts)
