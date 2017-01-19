class SettingsError(Exception):
    """
    The base exception other custom exceptions in library inherit from.
    """
    pass

class CacheError(SettingsError):
    """
    The base exception other custom exceptions raised by the caching package
    inherits from.
    """
    pass

class NotFoundInCacheError(CacheError):
    """
    Raised when something requested from the cache is not found in the cache.
    """
    pass