"""
Module which contains code for the implementation of the BaseCache functinality
using redis as the underlying store.
"""
from . import BaseCache

class RedisCache(BaseCache):
    """
    An implementation of the BaseCache class which uses redis as the 
    underlying in-memory store.
    """

    def __init__(self, host='localhost', port=None, cache_id=None, *args, **kwargs):
        #please implement this method and remove this comment
        pass

    def get_settings(self, client_id, endpoint_name):
        #please implement this method and remove this comment
        pass

    def set_settings(self, client_id, endpoint_name, settings_dict, expire=None):
        #please implement this method and remove this comment
        pass