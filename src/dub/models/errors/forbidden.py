"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from dub import utils
from dub.types import BaseModel
from enum import Enum
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class ForbiddenCode(str, Enum):
    r"""A short code indicating the error code returned."""
    FORBIDDEN = "forbidden"

class ForbiddenErrorTypedDict(TypedDict):
    code: ForbiddenCode
    r"""A short code indicating the error code returned."""
    message: str
    r"""A human readable explanation of what went wrong."""
    doc_url: NotRequired[str]
    r"""A link to our documentation with more details about this error code"""
    

class ForbiddenError(BaseModel):
    code: ForbiddenCode
    r"""A short code indicating the error code returned."""
    message: str
    r"""A human readable explanation of what went wrong."""
    doc_url: Optional[str] = None
    r"""A link to our documentation with more details about this error code"""
    
class ForbiddenData(BaseModel):
    error: ForbiddenError
    


class Forbidden(Exception):
    r"""The client does not have access rights to the content; that is, it is unauthorized, so the server is refusing to give the requested resource. Unlike 401 Unauthorized, the client's identity is known to the server."""
    data: ForbiddenData

    def __init__(self, data: ForbiddenData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, ForbiddenData)

