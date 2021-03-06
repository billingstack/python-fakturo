import logging

import requests

from fakturo.core import exceptions, utils


LOG = logging.getLogger(__name__)


class BaseClient(object):
    def __init__(self, url=None):
        url.rstrip('/')
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

    def wrap_api_call(self, function, path, status_code=200, *args, **kw):
        path = path.lstrip('/') if path else ''
        url = self.url + '/' + path
        LOG.debug('Wrapping request to %s' % url)

        wrapper = kw.get('wrapper', None)
        # NOTE: If we're passed a wrapper function by the caller, pass the
        # requests function to it along with path and other args...
        if wrapper and hasattr(wrapper, '__call__'):
            return wrapper(function, url, *args, **kw)

        response = function(url, *args, **kw)
        # NOTE: Make a function that can extract errors based on content type?
        if response.status_code != status_code:
            error = None
            if response.json:
                error = response.json.get('error', None)

            if not error:
                error = 'Remote error occured. Response Body:\n%s' % \
                    response.content
            raise exceptions.RemoteError(response.status_code, error)
        return response

    def get(self, *args, **kw):
        return self.wrap_api_call(self.requests.get, *args, **kw)

    def post(self, *args, **kw):
        return self.wrap_api_call(self.requests.post, *args, **kw)

    def put(self, *args, **kw):
        return self.wrap_api_call(self.requests.put, *args, **kw)

    def delete(self, *args, **kw):
        return self.wrap_api_call(self.requests.delete, *args, **kw)
