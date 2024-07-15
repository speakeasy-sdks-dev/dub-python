"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from dub.models.components import linkgeotargeting as components_linkgeotargeting
from dub.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import List, Optional, TypedDict, Union
from typing_extensions import Annotated, NotRequired


class UpsertLinkRequestBodyTypedDict(TypedDict):
    url: str
    r"""The destination URL of the short link."""
    domain: NotRequired[str]
    r"""The domain of the short link. If not provided, the primary domain for the workspace will be used (or `dub.sh` if the workspace has no domains)."""
    key: NotRequired[str]
    r"""The short link slug. If not provided, a random 7-character slug will be generated."""
    external_id: NotRequired[Nullable[str]]
    r"""This is the ID of the link in your database. If set, it can be used to identify the link in the future. Must be prefixed with `ext_` when passed as a query parameter."""
    prefix: NotRequired[str]
    r"""The prefix of the short link slug for randomly-generated keys (e.g. if prefix is `/c/`, generated keys will be in the `/c/:key` format). Will be ignored if `key` is provided."""
    track_conversion: NotRequired[bool]
    r"""Whether to track conversions for the short link."""
    archived: NotRequired[bool]
    r"""Whether the short link is archived."""
    public_stats: NotRequired[bool]
    r"""Whether the short link's stats are publicly accessible."""
    tag_id: NotRequired[Nullable[str]]
    r"""The unique ID of the tag assigned to the short link. This field is deprecated – use `tagIds` instead."""
    tag_ids: NotRequired[UpsertLinkTagIdsTypedDict]
    r"""The unique IDs of the tags assigned to the short link."""
    tag_names: NotRequired[UpsertLinkTagNamesTypedDict]
    r"""The unique name of the tags assigned to the short link (case insensitive)."""
    comments: NotRequired[Nullable[str]]
    r"""The comments for the short link."""
    expires_at: NotRequired[Nullable[str]]
    r"""The date and time when the short link will expire at."""
    expired_url: NotRequired[Nullable[str]]
    r"""The URL to redirect to when the short link has expired."""
    password: NotRequired[Nullable[str]]
    r"""The password required to access the destination URL of the short link."""
    proxy: NotRequired[bool]
    r"""Whether the short link uses Custom Social Media Cards feature."""
    title: NotRequired[Nullable[str]]
    r"""The title of the short link generated via `api.dub.co/metatags`. Will be used for Custom Social Media Cards if `proxy` is true."""
    description: NotRequired[Nullable[str]]
    r"""The description of the short link generated via `api.dub.co/metatags`. Will be used for Custom Social Media Cards if `proxy` is true."""
    image: NotRequired[Nullable[str]]
    r"""The image of the short link generated via `api.dub.co/metatags`. Will be used for Custom Social Media Cards if `proxy` is true."""
    rewrite: NotRequired[bool]
    r"""Whether the short link uses link cloaking."""
    ios: NotRequired[Nullable[str]]
    r"""The iOS destination URL for the short link for iOS device targeting."""
    android: NotRequired[Nullable[str]]
    r"""The Android destination URL for the short link for Android device targeting."""
    geo: NotRequired[Nullable[components_linkgeotargeting.LinkGeoTargetingTypedDict]]
    r"""Geo targeting information for the short link in JSON format `{[COUNTRY]: https://example.com }`."""
    do_index: NotRequired[bool]
    r"""Allow search engines to index your short link. Defaults to `false` if not provided. Learn more: https://d.to/noindex"""
    

class UpsertLinkRequestBody(BaseModel):
    url: str
    r"""The destination URL of the short link."""
    domain: Optional[str] = None
    r"""The domain of the short link. If not provided, the primary domain for the workspace will be used (or `dub.sh` if the workspace has no domains)."""
    key: Optional[str] = None
    r"""The short link slug. If not provided, a random 7-character slug will be generated."""
    external_id: Annotated[OptionalNullable[str], pydantic.Field(alias="externalId")] = UNSET
    r"""This is the ID of the link in your database. If set, it can be used to identify the link in the future. Must be prefixed with `ext_` when passed as a query parameter."""
    prefix: Optional[str] = None
    r"""The prefix of the short link slug for randomly-generated keys (e.g. if prefix is `/c/`, generated keys will be in the `/c/:key` format). Will be ignored if `key` is provided."""
    track_conversion: Annotated[Optional[bool], pydantic.Field(alias="trackConversion")] = False
    r"""Whether to track conversions for the short link."""
    archived: Optional[bool] = False
    r"""Whether the short link is archived."""
    public_stats: Annotated[Optional[bool], pydantic.Field(alias="publicStats")] = False
    r"""Whether the short link's stats are publicly accessible."""
    tag_id: Annotated[OptionalNullable[str], pydantic.Field(deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible.", alias="tagId")] = UNSET
    r"""The unique ID of the tag assigned to the short link. This field is deprecated – use `tagIds` instead."""
    tag_ids: Annotated[Optional[UpsertLinkTagIds], pydantic.Field(alias="tagIds")] = None
    r"""The unique IDs of the tags assigned to the short link."""
    tag_names: Annotated[Optional[UpsertLinkTagNames], pydantic.Field(alias="tagNames")] = None
    r"""The unique name of the tags assigned to the short link (case insensitive)."""
    comments: OptionalNullable[str] = UNSET
    r"""The comments for the short link."""
    expires_at: Annotated[OptionalNullable[str], pydantic.Field(alias="expiresAt")] = UNSET
    r"""The date and time when the short link will expire at."""
    expired_url: Annotated[OptionalNullable[str], pydantic.Field(alias="expiredUrl")] = UNSET
    r"""The URL to redirect to when the short link has expired."""
    password: OptionalNullable[str] = UNSET
    r"""The password required to access the destination URL of the short link."""
    proxy: Optional[bool] = False
    r"""Whether the short link uses Custom Social Media Cards feature."""
    title: OptionalNullable[str] = UNSET
    r"""The title of the short link generated via `api.dub.co/metatags`. Will be used for Custom Social Media Cards if `proxy` is true."""
    description: OptionalNullable[str] = UNSET
    r"""The description of the short link generated via `api.dub.co/metatags`. Will be used for Custom Social Media Cards if `proxy` is true."""
    image: OptionalNullable[str] = UNSET
    r"""The image of the short link generated via `api.dub.co/metatags`. Will be used for Custom Social Media Cards if `proxy` is true."""
    rewrite: Optional[bool] = False
    r"""Whether the short link uses link cloaking."""
    ios: OptionalNullable[str] = UNSET
    r"""The iOS destination URL for the short link for iOS device targeting."""
    android: OptionalNullable[str] = UNSET
    r"""The Android destination URL for the short link for Android device targeting."""
    geo: OptionalNullable[components_linkgeotargeting.LinkGeoTargeting] = UNSET
    r"""Geo targeting information for the short link in JSON format `{[COUNTRY]: https://example.com }`."""
    do_index: Annotated[Optional[bool], pydantic.Field(alias="doIndex")] = False
    r"""Allow search engines to index your short link. Defaults to `false` if not provided. Learn more: https://d.to/noindex"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["nullableOptional", "optional"]
        nullable_fields = ["nullableRequired", "nullableOptional"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields
                or (
                    k in optional_fields
                    and k in nullable_fields
                    and (
                        self.__pydantic_fields_set__.intersection({n})
                        or k in null_default_fields
                    )  # pylint: disable=no-member
                )
            ):
                m[k] = val

        return m
        

UpsertLinkTagIdsTypedDict = Union[str, List[str]]
r"""The unique IDs of the tags assigned to the short link."""


UpsertLinkTagIds = Union[str, List[str]]
r"""The unique IDs of the tags assigned to the short link."""


UpsertLinkTagNamesTypedDict = Union[str, List[str]]
r"""The unique name of the tags assigned to the short link (case insensitive)."""


UpsertLinkTagNames = Union[str, List[str]]
r"""The unique name of the tags assigned to the short link (case insensitive)."""

