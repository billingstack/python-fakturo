import logging
from urlparse import urlparse


import requests

from fakturo.core import exceptions, utils


LOG = logging.getLogger(__name__)


class BaseClient(object):
    def __init__(self, url=None):
        self.requests = self.get_requests()

    def _ensure_url(self, args):
        parsed = urlparse(args['url'])
        if not parsed.scheme:
            args['url'] = self.url + parsed.path

    def get_requests(self, headers={}, args_hooks=[], pre_request_hooks=[]):
        if not 'Content-Type' in headers:
            headers['Content-Type'] = 'application/json'

        if not self._ensure_url in args_hooks:
            args_hooks.append(self._ensure_url)

        if utils.log_request not in pre_request_hooks:
            pre_request_hooks.insert(0, utils.log_request)

        session = requests.Session()
        session.hooks = dict(
            args=args_hooks,
            pre_request=pre_request_hooks)
        session.headers.update(headers)
        return session

    def wrap_api_call(self, function, *args, **kw):
        wrapper = kw.get('wrapper', None)
        # NOTE: If we're passed a wrapper function by the caller, pass the
        # requests function to it along with path and other args...
        if wrapper and hasattr(wrapper, '__call__'):
            return wrapper(function, *args, **kw)

        response = function(*args, **kw)
        if response.status_code != 200:
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
