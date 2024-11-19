# Standard Library
import re
from datetime import datetime, timedelta

# Third Party Library
import numpy as np


def iso2int(date: str) -> int:
    start_epoch = (1970, 1, 1, 3, 0)
    date = datetime.fromisoformat(date)
    return int((date - datetime(*start_epoch)).total_seconds() * 1000)


def int2iso(timestamp: int) -> str:
    return (datetime.fromtimestamp(timestamp / 1000)).isoformat()


def iso2int_nsi(date: str) -> int:
    return int(iso2int(date.rpartition('.')[0]))


def hours2ms(time_in_hours: int) -> str:
    return time_in_hours * 60 * 60 * 1000


def ms2hours(time_in_ms: int) -> str:
    return time_in_ms / (60 * 60 * 1000)


def str2days(str_days: str) -> float:
    count_days = re.search(r'(\d+)', rf'{str_days}')
    return float(count_days[0])


def iso_shift_date(date: str, time_delta_seconds: int) -> str:
    return datetime.fromisoformat(date) + timedelta(seconds=time_delta_seconds)


def int_shift_date(date: int | np.ndarray, time_delta_seconds: int) -> int | np.ndarray:
    return date + time_delta_seconds * 1000
