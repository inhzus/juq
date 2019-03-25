# -*- coding: utf-8 -*-
# created by inhzus


class JuqException(Exception):
    pass


class HandlerException(JuqException):
    pass


class MissingFieldsException(HandlerException):
    pass


class RequestException(JuqException):
    """Exceptions occurred in request.py"""
    pass


class NotFoundException(RequestException):
    pass


class BadRequestException(RequestException):
    pass


class UnauthorizedException(RequestException):
    pass


class ForbiddenException(RequestException):
    pass


class InternalServerException(RequestException):
    pass


STATUS_EXCEPTION_MAP = {
    # 400: BadRequestException,
    **dict.fromkeys((400, 422), BadRequestException),
    401: UnauthorizedException,
    403: ForbiddenException,
    404: NotFoundException,
    500: InternalServerException
}

EXCEPTION_MESSAGE_MAP = {
    BadRequestException: 'Parameters incorrect or necessary info missing.',
    UnauthorizedException: 'Operating unauthorized. Configure TOKEN at "~/.yuq" first.',
    ForbiddenException: 'Correspond permission missing.',
    NotFoundException: 'Not found.',
    InternalServerException: 'Internal server error.'
}
