
from typing import List, Optional
from fastapi import FastAPI, Path, Query

async def params_fourpoint_algorithm(fourpoints: List[List[int]], \
                                     test: Optional[int] = None):
    """
    """
    assert len(fourpoints) == 4
    for point in fourpoints:
        assert  len(point) == 2

    ret = {
        "fourpoints": fourpoints, \
        "test": test, \
    }
    return ret