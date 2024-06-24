#!/usr/bin/env python3
"""pagination"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """index range
    Args
    page: int
    page_size: int

    Return
    Tuple
    """
    idx_end = page * page_size
    idx_strt = idx_end - page_size

    return idx_strt, idx_end


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get page
        Args
        page: int
        page_size: int

        Return
        List
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        idxs_strt, idxs_end = index_range(page, page_size)
        dataset = self.dataset()

        if idxs_strt >= len(dataset) or idxs_end <= 0:
            return []

        return dataset[int(idxs_strt):int(idxs_end)]
