"""File 4 creating and adding new filters."""
# Standard Library
from abc import ABC, abstractmethod
from math import factorial
from typing import List, Tuple

# Third Party Library
import numpy as np
from src.internal.converters.date_converter import iso2int
from src.internal.converters.ts_converter import (
    ts2dates,
    ts2numpy,
    ts2vals,
)
from src.internal.converters.date_converter import (
    ms2hours,
)


def sliding_window(ts: np.ndarray, window_size: int) -> np.ndarray:
    return np.convolve(ts2vals(ts), np.ones(window_size), 'same') / window_size


class AbstractFilter(ABC):
    """Abstract Filter."""

    @abstractmethod
    def apply_filter(self, ts: List[Tuple]) -> List:
        return ts


class NoFilter(AbstractFilter):
    """Returns TS."""

    def apply_filter(self, ts: List[Tuple]) -> List:
        return ts


+


class Square(AbstractFilter):
    """Returns Squared List."""

    def sq(self, data: np.ndarray):
        data = list(data)
        for i in range(len(data)):
            data[i] = int(data[i]) ** 2
        return data

    def apply_filter(self, ts: List[Tuple]) -> np.ndarray:
        ts = ts2numpy(ts)
        return np.vstack([ts2dates(ts), self.sq(ts2vals(ts))]).T


class Slice(AbstractFilter):
    """Returns Slise of TimeSeries."""

    def apply_filter(self, ts: List[Tuple], up: float, down: float) -> np.ndarray:
        ts = ts2numpy(ts)
        ts_values = ts2vals(ts)
        mask = (down < ts_values), (ts_values < up)
        return ts[np.logical_and(*mask)]


class SliceByDate(AbstractFilter):
    def apply_filter(self, ts: List[Tuple], date_intervals: List[Tuple[str, str]]) -> np.ndarray:
        ts = ts2numpy(ts)

        for start, end in date_intervals:
            start = iso2int(start)
            end = iso2int(end)

            ts_dates = ts2dates(ts)

            mask = (start > ts_dates), (ts_dates > end)
            ts = ts[np.logical_or(*mask)]

        return ts


class MovingAverage(AbstractFilter):
    """Returns Moving Average of TimeSeries."""

    def apply_filter(self, ts: List[Tuple], window_size: int = 3) -> np.ndarray:
        mov_average = sliding_window(ts, window_size)
        return np.vstack([ts2dates(ts), np.round(mov_average, 2)]).T


class IntegralFilter(AbstractFilter):
    """Returns Integral of TimeSeries."""

    def apply_filter(self, ts: List[Tuple]) -> np.ndarray:
        ts = ts2numpy(ts)
        
        difference_dates = ms2hours(np.concatenate([[0], np.diff(ts2dates(ts))]))

        cumulative_values = sliding_window(ts, window_size=2)
        cumulative_values[0] = 0
        cumulative_values = cumulative_values * difference_dates
        cumulative_values = cumulative_values.cumsum()
        return np.vstack([ts2dates(ts), cumulative_values]).T


class ExponentialSmoothing(AbstractFilter):
    """Returns ExponentialSmoothing of TimeSeries."""

    def apply_filter(self, ts: List[Tuple], alpha: float = 0.2) -> np.ndarray:
        ts_values = np.copy(ts2vals(ts))
        ts_values[1:] = alpha * ts_values[1:]

        for idx in range(1, ts_values.shape[0]):
            ts_values[idx] = ts_values[idx] + (1-alpha) * ts_values[idx-1]
        return np.vstack([ts2dates(ts), ts_values]).T


class DoubleExponentialSmoothing(AbstractFilter):
    """Returns DoubleExponentialSmoothing of TimeSeries."""

    def apply_filter(self, ts: List[Tuple], alpha: float = 0.2, beta: float = 0.2) -> np.ndarray:
        ts_values = np.copy(ts2vals(ts))
        count_values = ts_values.shape[0]
        level = np.zeros(count_values)
        trend = np.zeros(count_values)
        forecast = np.zeros(count_values)

        level[0] = ts_values[0]
        trend[0] = ts_values[1] - ts_values[0]
        ts_values[1:] = alpha * ts_values[1:]

        for idx in range(1, count_values):
            level[idx] = ts_values[idx] + (1 - alpha) * (level[idx-1] + trend[idx-1])
            trend[idx] = beta * (level[idx] - level[idx-1]) + (1 - beta) * trend[idx-1]
            forecast[idx] = level[idx-1] + trend[idx-1]

        return np.vstack([ts2dates(ts), forecast]).T


class MedianFilter(AbstractFilter):
    """Returns MedianFilter of TimeSeries."""

    def apply_filter(self, ts: List[Tuple], window_size: int = 3) -> np.ndarray:
        ts_values = ts2vals(ts)
        padded_values = np.pad(ts_values, window_size // 2, mode="constant")
        padded_values = np.lib.stride_tricks.sliding_window_view(padded_values, window_size)
        return np.vstack([ts2dates(ts), np.median(padded_values, axis=1)]).T


class HampelFilter(AbstractFilter):
    """Returns HampelFilter of TimeSeries."""

    def apply_filter(self, ts: List[Tuple], window_size: int = 3, n_sigmas: int = 3) -> np.ndarray:
        ts_values = np.copy(ts2vals(ts))
        ts_len = ts_values.shape[0]
        scale_factor = 1.4826

        window = np.lib.stride_tricks.as_strided(
            x=ts_values,
            shape=(ts_len - 2 * window_size, 2 * window_size),
            strides=(ts_values.strides[0], ts_values.strides[0]),
        )
        medians = np.median(window, axis=1)
        mad = np.abs(window - medians.reshape(-1, 1))
        mad = scale_factor * np.median(mad, axis=1)

        mask = np.abs(ts_values[window_size:ts_len-window_size] - medians)
        mask = mask > n_sigmas * mad
        mask = np.where(mask, medians, ts_values[window_size:ts_len-window_size])
        ts_values[window_size:ts_len-window_size] = mask

        return np.vstack([ts2dates(ts), ts_values]).T


class SavGolFilter(AbstractFilter):
    """Returns Savitzky-Golay Filter of TimeSeries."""

    def apply_filter(
        self,
        ts: List[Tuple],
        window_size: int = 5,
        polyorder: int = 2,
        deriv: int = 0,
        rate: int = 1,
    ) -> np.ndarray:
        ts_values = np.copy(ts2vals(ts))
        # precompute coefficients
        coef_b = np.arange(-window_size, window_size+1)
        coef_b = np.tile(coef_b, (polyorder + 1, 1)).T
        coef_b = np.mat(np.power(coef_b, np.arange(polyorder + 1)))

        coef_m = rate**deriv * factorial(deriv)
        coef_m = np.linalg.pinv(coef_b).A[deriv] * coef_m

        firstvals = np.flipud(ts_values[1:window_size+1])
        firstvals -= ts_values[0]
        firstvals = ts_values[0] - np.abs(firstvals)

        lastvals = np.flipud(ts_values[-window_size-1:-1])
        lastvals -= ts_values[-1]
        lastvals = ts_values[-1] + np.abs(lastvals)

        ts_values = np.concatenate((firstvals, ts_values, lastvals))
        ts_values = np.convolve(coef_m[::-1], ts_values, mode='valid')
        return np.vstack([ts2dates(ts), ts_values]).T


class QuantileFilter(AbstractFilter):
    """Returns QuantileFilter of TimeSeries."""

    def apply_filter(self, ts: List[Tuple], percent: float = 5) -> np.ndarray:
        ts = ts2numpy(ts)
        ts_values = ts2vals(ts)
        q_low = np.quantile(ts_values, percent/100)
        q_high = np.quantile(ts_values, 1 - percent/100)
        mask = (ts_values >= q_low), (ts_values <= q_high)
        return ts[np.logical_and(*mask)]


class ControlChart(AbstractFilter):
    """Returns ControlChart of TimeSeries."""

    def apply_filter(self, ts: List[Tuple], n_groups: int = 5, threshold: float = 0.2) -> np.ndarray:
        ts = ts2numpy(ts)
        ts_values = ts[:, 1]
        ts = ts[np.argsort(ts_values)]

        norm_data = (ts_values - np.min(ts_values))
        norm_data = norm_data / (np.max(ts_values) - np.min(ts_values))
        norm_data = np.vstack((ts2dates(ts), norm_data)).T

        data_groups = np.array_split(norm_data, n_groups)
        deviation = [np.mean(ts2vals(group)) for group in data_groups]
        deviation = np.abs(deviation - np.mean(ts2vals(norm_data)))

        indices_to_keep = []
        for idx, group in enumerate(data_groups):
            if deviation[idx] < threshold:
                indices_to_keep.extend(np.arange(len(group)) + idx * len(group))
        ts = ts[indices_to_keep]

        return ts[np.argsort(ts2dates(ts))]


class ShiftDateFilter(AbstractFilter):
    """Returns updated date timeseries."""

    def apply_filter(self, ts: List[Tuple], shift_delta: int) -> np.ndarray:
        ts = ts2numpy(ts)

        time = ts[:, 0] + shift_delta
        vals = ts[:, 1]

        return np.column_stack((time, vals))
