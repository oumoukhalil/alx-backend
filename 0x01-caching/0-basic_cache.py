#!/usr/bin/python3
""" BaseCaching module
"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ basic cache class

    BaseCaching: parent
    """
    def __init__(delf):
        super().__init__()

    def put(self, key, item):
        """add an item in the cache

        Arguments
        ---------
        key: str
        item: str

        Return
        ------
        None
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key

        Arguments
        --------
        key: str

        Return:
        str or None
        """
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
