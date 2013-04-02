import logging

from stevedore.driver import DriverManager


LOG = logging.getLogger(__name__)


NAMESPACE = 'fakturo.provider'


class ProviderBase(object):
    api = None
    client = None

    def __init__(self):
        pass

    def extend_parser(self, name, parser):
        """
        Extend a Command with options from the Provider API
        """
        try:
            func = getattr(self.api, name + '_parser')
        except AttributeError:
            LOG.warn('Command %s doesn\'t extend options', name)
            return
        func(parser)

    def get_api(self, parsed_args, command):
        """
        Get a Provider Command api
        """
        raise NotImplementedError

    def get_client(self, *args, **kw):
        """
        Get a Client object
        """
        return self.client(*args, **kw)


def get_provider(name, invoke_args=(), invoke_kwds={}):
    """
    Get a provider based on the self.provider_name propery
    """
    mgr = DriverManager(NAMESPACE, name, invoke_on_load=True,
                        invoke_args=invoke_args, invoke_kwds=invoke_kwds)
    return mgr.driver
