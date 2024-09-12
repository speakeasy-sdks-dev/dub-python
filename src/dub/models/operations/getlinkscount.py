"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel
from dub.utils import FieldMetadata, QueryParamMetadata
from enum import Enum
import pydantic
from typing import List, Optional, TypedDict, Union
from typing_extensions import Annotated, NotRequired


GetLinksCountQueryParamTagIdsTypedDict = Union[str, List[str]]
r"""The tag IDs to filter the links by."""


GetLinksCountQueryParamTagIds = Union[str, List[str]]
r"""The tag IDs to filter the links by."""


GetLinksCountQueryParamTagNamesTypedDict = Union[str, List[str]]
r"""The unique name of the tags assigned to the short link (case insensitive)."""


GetLinksCountQueryParamTagNames = Union[str, List[str]]
r"""The unique name of the tags assigned to the short link (case insensitive)."""


class Three(str, Enum):
    USER_ID = "userId"


class Two(str, Enum):
    TAG_ID = "tagId"


class One(str, Enum):
    DOMAIN = "domain"


GroupByTypedDict = Union[One, Two, Three]
r"""The field to group the links by."""


GroupBy = Union[One, Two, Three]
r"""The field to group the links by."""


class GetLinksCountRequestTypedDict(TypedDict):
    domain: NotRequired[str]
    r"""The domain to filter the links by. E.g. `ac.me`. If not provided, all links for the workspace will be returned."""
    tag_id: NotRequired[str]
    r"""The tag ID to filter the links by. This field is deprecated – use `tagIds` instead."""
    tag_ids: NotRequired[GetLinksCountQueryParamTagIdsTypedDict]
    r"""The tag IDs to filter the links by."""
    tag_names: NotRequired[GetLinksCountQueryParamTagNamesTypedDict]
    r"""The unique name of the tags assigned to the short link (case insensitive)."""
    search: NotRequired[str]
    r"""The search term to filter the links by. The search term will be matched against the short link slug and the destination url."""
    user_id: NotRequired[str]
    r"""The user ID to filter the links by."""
    show_archived: NotRequired[bool]
    r"""Whether to include archived links in the response. Defaults to `false` if not provided."""
    with_tags: NotRequired[bool]
    r"""Whether to include tags in the response. Defaults to `false` if not provided."""
    group_by: NotRequired[GroupByTypedDict]
    r"""The field to group the links by."""


class GetLinksCountRequest(BaseModel):
    domain: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The domain to filter the links by. E.g. `ac.me`. If not provided, all links for the workspace will be returned."""

    tag_id: Annotated[
        Optional[str],
        pydantic.Field(alias="tagId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The tag ID to filter the links by. This field is deprecated – use `tagIds` instead."""

    tag_ids: Annotated[
        Optional[GetLinksCountQueryParamTagIds],
        pydantic.Field(alias="tagIds"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The tag IDs to filter the links by."""

    tag_names: Annotated[
        Optional[GetLinksCountQueryParamTagNames],
        pydantic.Field(alias="tagNames"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The unique name of the tags assigned to the short link (case insensitive)."""

    search: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The search term to filter the links by. The search term will be matched against the short link slug and the destination url."""

    user_id: Annotated[
        Optional[str],
        pydantic.Field(alias="userId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The user ID to filter the links by."""

    show_archived: Annotated[
        Optional[bool],
        pydantic.Field(alias="showArchived"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = True
    r"""Whether to include archived links in the response. Defaults to `false` if not provided."""

    with_tags: Annotated[
        Optional[bool],
        pydantic.Field(alias="withTags"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = True
    r"""Whether to include tags in the response. Defaults to `false` if not provided."""

    group_by: Annotated[
        Optional[GroupBy],
        pydantic.Field(alias="groupBy"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The field to group the links by."""
