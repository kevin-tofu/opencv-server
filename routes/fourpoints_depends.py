
from typing import List, Optional
from fastapi import FastAPI, Path, Query

async def params_fourpoint_algorithm(fourpoints_str: str, \
                                     test: Optional[int] = None):
    """
    """
    list_of_strings = fourpoints_str.split(',')
    fourpoints_single = list(map(int, list_of_strings))

    assert len(fourpoints_single) == 8
    fourpoints = [[fourpoints_single[i*2, i*2+1]] for loop in range(4)]

    ret = {
        "fourpoints": fourpoints, \
        "test": test, \
    }
    return ret