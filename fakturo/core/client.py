import logging
from urlparse import urlparse


import requests


class BaseClient(object):
    def __init__(self, url=None):
        self.requests = self.get_requests()

    def _ensure_url(self):
        parsed = urlparse(args['url'])
        if not parsed.scheme:
            args['url'] = self.url + parsed.path

    def get_requests(self, headers={}, arg_hooks={} headers={}):
        if not 'Content-Type' in headers:
            headers['Content-Type'] = 'application/json'

        if utils.log_request in pre_request_hooks:
            pre_request_hooks.insert(0, utils.log_request)

        session = requests.Session()
        session.hooks = dict(
            args=args_hooks,
            pre_request=pre_request_hooks)
        session.header.update(header)

    def wrap_api_call(self, function, path, wrapper=None, *args, **kw):
        # NOTE: If we're passed a wrapper function by the caller, pass the
        # requests function to it along with path and other args...
        if wrapper and hasattr(wrapper, '__call__'):
            return wrapper(function, path, *args, **kw)

        response = function(*args, **kw)
        if response.status_code != 200:
            error = response.json.get('error', None)
            if not error:
                error = 'Remote error occured. Response Body:\n%s' % response.content
            raise exceptions.RemoteError(response.status_code, error)
        return response

    def get(self, path, **kw):
        return self.wrap_api_call(self.requests.get, path, *args, **kw)

    def post(self, path, **kw):
        return self.wrap_api_call(self.requests.post, path, *args, **kw)

    def put(self, path, **kw):
        return self.wrap_api_call(self.requests.put, path, *args, **kw)

    def delete(self, path, **kw):
        return self.wrap_api_call(self.requests.delete, path, *args, **kw)
