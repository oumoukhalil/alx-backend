#!/usr/bin/env python3
"""lru cache replacement policy"""
from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRU cache
    inherit from BaseCaching class
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """put data in chache

        Arguments
        ---------
        key: str
        item: any

        Return
        ------
        None
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                _key = self.cache_data.popitem()
                print(f"DISCARD: {_key[0]}")
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """get iten by key

        Argument
        --------
        key: str

        Return
        ------

        self.cache_data[key] or None
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
            return self.cache_data[key]

        return None
