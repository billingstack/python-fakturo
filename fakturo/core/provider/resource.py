class BaseResource(object):
    def __init__(self, client):
        self.client = client

    def create(self, *args, **kw):
        raise NotImplementedError

    def list(self, *args, **kw):
        raise NotImplementedError

    def get(self, *args, **kw):
        raise NotImplementedError

    def update(self, *args, **kw):
        raise NotImplementedError

    def delete(self, *args, **kw):
        raise NotImplementedError
