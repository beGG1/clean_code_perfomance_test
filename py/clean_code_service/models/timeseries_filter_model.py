from typing import Optional

from pydantic import BaseModel

class FilterModel(BaseModel):
    ts_algorithm: str
    input_kwargs: Optional[dict]

class TimeSeriesFilterModel(BaseModel):
    ts: list[tuple[str, int]]
    filters: Optional[list[FilterModel]]
    
class TimeSeriesFilterModelReturn(BaseModel):
    ts: list[tuple[str, int]]
    status: int
    