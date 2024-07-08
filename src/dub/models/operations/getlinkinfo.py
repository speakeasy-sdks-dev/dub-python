"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel
from dub.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetLinkInfoGlobalsTypedDict(TypedDict):
    workspace_id: NotRequired[str]
    

class GetLinkInfoGlobals(BaseModel):
    workspace_id: Annotated[Optional[str], pydantic.Field(deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible.", alias="workspaceId"), FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    

class GetLinkInfoRequestTypedDict(TypedDict):
    domain: NotRequired[str]
    key: NotRequired[str]
    r"""The key of the link to retrieve. E.g. for `d.to/github`, the key is `github`."""
    link_id: NotRequired[str]
    r"""The unique ID of the short link."""
    external_id: NotRequired[str]
    r"""This is the ID of the link in the your database. Must be prefixed with `ext_` when passed as a query parameter."""
    

class GetLinkInfoRequest(BaseModel):
    domain: Annotated[Optional[str], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    key: Annotated[Optional[str], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""The key of the link to retrieve. E.g. for `d.to/github`, the key is `github`."""
    link_id: Annotated[Optional[str], pydantic.Field(alias="linkId"), FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""The unique ID of the short link."""
    external_id: Annotated[Optional[str], pydantic.Field(alias="externalId"), FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""This is the ID of the link in the your database. Must be prefixed with `ext_` when passed as a query parameter."""
    
