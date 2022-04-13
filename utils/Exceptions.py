class NotFound(Exception):
    status_code = 404


class BadRequest(Exception):
    status_code = 400
