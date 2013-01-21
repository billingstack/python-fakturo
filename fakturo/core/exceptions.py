class RemoteError(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        super(RemoteError, self).__init__(message)


class ResourceNotFound(RemoteError):
    pass


class Unknown(RemoteError):
    pass


class Forbidden(RemoteError):
    pass


class Conflict(RemoteError):
    pass


class NotFound(RemoteError):
    pass


class CommandError(Exception):
    pass


class CommandNotSupported(CommandError):
    pass
