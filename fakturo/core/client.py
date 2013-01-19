import logging
from urlparse import urlparse


import requests

from fakturo.core import exceptions, utils


LOG = logging.getLogger(__name__)


class BaseClient(object):
    def __init__(self, url=None):
        self.url = url

        self.requests = self.get_requests()

    def get_requests(self, headers={}, args_hooks=[], pre_request_hooks=[]):
        if not 'Content-Type' in headers:
            headers['Content-Type'] = 'application/json'

        pre_request_hooks = pre_request_hooks + [utils.log_request]

        session = requests.Session()
        session.hooks = dict(
            args=args_hooks,
            pre_request=pre_request_hooks)
        session.headers.update(headers)
        return session

    def wrap_api_call(self, function, path, *args, **kw):
        path = self.url + '/' + path

        wrapper = kw.get('wrapper', None)
        # NOTE: If we're passed a wrapper function by the caller, pass the
        # requests function to it along with path and other args...
        if wrapper and hasattr(wrapper, '__call__'):
            return wrapper(function, path, *args, **kw)

        response = function(path, *args, **kw)
        # NOTE: Make a function that can extract errors based on content type?
        if response.status_code != 200:
            error = None
            if response.json:
                error = response.json.get('error', None)

            if not error:
                error = 'Remote error occured. Response Body:\n%s' % response.content
            raise exceptions.RemoteError(response.status_code, error)
        return response

    def get(self, path, *args, **kw):
        return self.wrap_api_call(self.requests.get, path, *args, **kw)

    def post(self, path, *args, **kw):
        return self.wrap_api_call(self.requests.post, path, *args, **kw)

    def put(self, path, *args, **kw):
        return self.wrap_api_call(self.requests.put, path, *args, **kw)

    def delete(self, path, *args, **kw):
        return self.wrap_api_call(self.requests.delete, path, *args, **kw)
