"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from dub import utils
from dub.types import BaseModel
from enum import Enum
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class ConflictCode(str, Enum):
    r"""A short code indicating the error code returned."""

    CONFLICT = "conflict"


class ConflictErrorTypedDict(TypedDict):
    code: ConflictCode
    r"""A short code indicating the error code returned."""
    message: str
    r"""A human readable explanation of what went wrong."""
    doc_url: NotRequired[str]
    r"""A link to our documentation with more details about this error code"""


class ConflictError(BaseModel):
    code: ConflictCode
    r"""A short code indicating the error code returned."""

    message: str
    r"""A human readable explanation of what went wrong."""

    doc_url: Optional[str] = None
    r"""A link to our documentation with more details about this error code"""


class ConflictData(BaseModel):
    error: ConflictError


class Conflict(Exception):
    r"""This response is sent when a request conflicts with the current state of the server."""

    data: ConflictData

    def __init__(self, data: ConflictData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, ConflictData)
