"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel
from dub.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import List, TypedDict
from typing_extensions import Annotated


class BulkDeleteLinksRequestTypedDict(TypedDict):
    link_ids: List[str]
    r"""Comma-separated list of link IDs to delete. Maximum of 100 IDs. Non-existing IDs will be ignored."""


class BulkDeleteLinksRequest(BaseModel):
    link_ids: Annotated[
        List[str],
        pydantic.Field(alias="linkIds"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ]
    r"""Comma-separated list of link IDs to delete. Maximum of 100 IDs. Non-existing IDs will be ignored."""


class BulkDeleteLinksResponseBodyTypedDict(TypedDict):
    r"""The deleted links count."""

    deleted_count: float
    r"""The number of links deleted."""


class BulkDeleteLinksResponseBody(BaseModel):
    r"""The deleted links count."""

    deleted_count: Annotated[float, pydantic.Field(alias="deletedCount")]
    r"""The number of links deleted."""
