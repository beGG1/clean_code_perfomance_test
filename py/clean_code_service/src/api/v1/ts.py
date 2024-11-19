from fastapi import APIRouter

from models.timeseries_filter_model import TimeSeriesFilterModel, TimeSeriesFilterModelReturn
from src.handlers.ts_filter_handlers import filter_ts_handler


router = APIRouter(prefix="/ts", tags=["ts"])

@router.post("/filter")
def filter_ts(data: TimeSeriesFilterModel) -> TimeSeriesFilterModelReturn:
    ts = filter_ts_handler(data.ts, data.filters)
    return TimeSeriesFilterModelReturn(
        ts=ts,
        status=200
    )
