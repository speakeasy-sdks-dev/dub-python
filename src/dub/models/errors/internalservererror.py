"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from dub import utils
from dub.types import BaseModel
from enum import Enum
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class InternalServerErrorCode(str, Enum):
    r"""A short code indicating the error code returned."""

    INTERNAL_SERVER_ERROR = "internal_server_error"


class InternalServerErrorErrorTypedDict(TypedDict):
    code: InternalServerErrorCode
    r"""A short code indicating the error code returned."""
    message: str
    r"""A human readable explanation of what went wrong."""
    doc_url: NotRequired[str]
    r"""A link to our documentation with more details about this error code"""


class InternalServerErrorError(BaseModel):
    code: InternalServerErrorCode
    r"""A short code indicating the error code returned."""

    message: str
    r"""A human readable explanation of what went wrong."""

    doc_url: Optional[str] = None
    r"""A link to our documentation with more details about this error code"""


class InternalServerErrorData(BaseModel):
    error: InternalServerErrorError


class InternalServerError(Exception):
    r"""The server has encountered a situation it does not know how to handle."""

    data: InternalServerErrorData

    def __init__(self, data: InternalServerErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, InternalServerErrorData)
