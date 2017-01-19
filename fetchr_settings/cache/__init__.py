from fetchr_settings.exceptions import NotFoundInCacheError

_method_not_implemented_msg = 'method not implemented'

class BaseCache:
    """
    Base class which specifies the interface for accessing a cache. The
    cache could be implemented using any suitable caching technology.

    Keyword Args:
        host(str): the host name of the machine we communicate with the
            cache store from.
        port(int): the port number on the machine the cache store runs on.
        cache_id(str): a unique identifier which can be used to select 
            a DB in the underlying cache service. In redis, this should be
            the database which data will be stored on.
    """
    def __init__(self, host='localhost', port=None, cache_id=None, *args, **kwargs):
        raise NotImplementedError("This is an abstract base class.")

    def get_settings(self, client_id, endpoint_name):
        """
        Gets a settings dictionary of an endpoint for a certain client.

        Args:
            client_id(str): the unique id of the client the settings is 
                meant to be gotten for.
            endpoint_name(str): the endpoint name the settings is to be 
                retrieved for.

        Returns:
            dict: a settings dict if the settings for the client and endpoint 
            exists already in the cache. Raises NotFoundInCacheError if the 
            settings requested is not found.

        Raises:
            NotFoundInCacheError: raised when the requested settings dict
                is not found in the cache.
        """
        raise NotImplementedError(_method_not_implemented_msg)

    def set_settings(self, client_id, endpoint_name, settings_dict, expire=None):
        """
        Stores a dict in the underlying cache.This settings dict may be 
        serialized before being stored in the underlying cache system.

        Args:
            client_id(str): the unique id of the client the settings is
                meant to be gotten for.
            endpoint_name(str): the endpoint name the settings is to be 
                retrieved for.
            settings(dict): a dictionary containing the settings to be stored
                in the cache.

        Keyword Args:
            expire(int): (optional)the number of seconds the settings dict
                should exist in the cache before it becomes invalid.

        Returns:
            bool: True if the dict could be cached, False otherwise.
        """
        raise NotImplementedError(_method_not_implemented_msg)