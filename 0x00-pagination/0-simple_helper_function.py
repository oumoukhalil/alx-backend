#!/usr/bin/env python3
""" pagination """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index rang

    Args
    ----
    page: int
       page number
    page_size: int
       page size

    Return
    ------
    a tuple of size two
    containing a start index and an end index
    """
    int: index_end
    int: index_start

    index_end = page * page_size
    index_start = index_end - page_size
    return index_start, index_end
