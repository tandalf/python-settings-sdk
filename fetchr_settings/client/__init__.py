from fetchr_settings.cache.redis import RedisCache

class FetchrSettings:
    """
    Client class used in communicating with fetchr's settings micro-service
    api. 

    Keyword Args:
        cache_class(BaseCache): (optional)an implementation of the BaseCache 
            class which will be used for caching settings. If None is 
            provided, the requests to the settings service would not be cached
    """
    def __int__(self, auth_token, cache_class=None):
        pass

    def get_api_settings(self, api_name):
        """
        Makes a get request to the settings api, getting the the settings
        configuration for the api name provided.

        Args:
            api_name(str): the name of the api whose setting is to be 
                retrieved.
        """

    def post_api_settings(self, api_name, settings_dict):
        pass