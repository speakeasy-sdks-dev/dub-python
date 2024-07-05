"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import linkgeotargeting as components_linkgeotargeting
from dataclasses_json import Undefined, dataclass_json
from dub import utils
from typing import List, Optional, Union


@dataclasses.dataclass
class UpdateLinkGlobals:
    workspace_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'workspaceId', 'style': 'form', 'explode': True }})
    r"""Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateLinkRequestBody:
    UNSET='__SPEAKEASY_UNSET__'
    url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url') }})
    r"""The destination URL of the short link."""
    domain: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domain'), 'exclude': lambda f: f is None }})
    r"""The domain of the short link. If not provided, the primary domain for the workspace will be used (or `dub.sh` if the workspace has no domains)."""
    key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key'), 'exclude': lambda f: f is None }})
    r"""The short link slug. If not provided, a random 7-character slug will be generated."""
    external_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('externalId'), 'exclude': lambda f: f is UpdateLinkRequestBody.UNSET }})
    r"""This is the ID of the link in your database. If set, it can be used to identify the link in the future. Must be prefixed with `ext_` when passed as a query parameter."""
    prefix: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prefix'), 'exclude': lambda f: f is None }})
    r"""The prefix of the short link slug for randomly-generated keys (e.g. if prefix is `/c/`, generated keys will be in the `/c/:key` format). Will be ignored if `key` is provided."""
    track_conversion: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trackConversion'), 'exclude': lambda f: f is None }})
    r"""Whether to track conversions for the short link."""
    archived: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('archived'), 'exclude': lambda f: f is None }})
    r"""Whether the short link is archived."""
    public_stats: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('publicStats'), 'exclude': lambda f: f is None }})
    r"""Whether the short link's stats are publicly accessible."""
    tag_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tagId'), 'exclude': lambda f: f is UpdateLinkRequestBody.UNSET }})
    r"""The unique ID of the tag assigned to the short link. This field is deprecated – use `tagIds` instead.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    tag_ids: Optional[UpdateLinkTagIds] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tagIds'), 'exclude': lambda f: f is None }})
    r"""The unique IDs of the tags assigned to the short link."""
    tag_names: Optional[UpdateLinkTagNames] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tagNames'), 'exclude': lambda f: f is None }})
    r"""The unique name of the tags assigned to the short link (case insensitive)."""
    comments: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('comments'), 'exclude': lambda f: f is UpdateLinkRequestBody.UNSET }})
    r"""The comments for the short link."""
    expires_at: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expiresAt'), 'exclude': lambda f: f is UpdateLinkRequestBody.UNSET }})
    r"""The date and time when the short link will expire at."""
    expired_url: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expiredUrl'), 'exclude': lambda f: f is UpdateLinkRequestBody.UNSET }})
    r"""The URL to redirect to when the short link has expired."""
    password: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is UpdateLinkRequestBody.UNSET }})
    r"""The password required to access the destination URL of the short link."""
    proxy: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('proxy'), 'exclude': lambda f: f is None }})
    r"""Whether the short link uses Custom Social Media Cards feature."""
    title: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is UpdateLinkRequestBody.UNSET }})
    r"""The title of the short link generated via `api.dub.co/metatags`. Will be used for Custom Social Media Cards if `proxy` is true."""
    description: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is UpdateLinkRequestBody.UNSET }})
    r"""The description of the short link generated via `api.dub.co/metatags`. Will be used for Custom Social Media Cards if `proxy` is true."""
    image: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('image'), 'exclude': lambda f: f is UpdateLinkRequestBody.UNSET }})
    r"""The image of the short link generated via `api.dub.co/metatags`. Will be used for Custom Social Media Cards if `proxy` is true."""
    rewrite: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rewrite'), 'exclude': lambda f: f is None }})
    r"""Whether the short link uses link cloaking."""
    ios: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ios'), 'exclude': lambda f: f is UpdateLinkRequestBody.UNSET }})
    r"""The iOS destination URL for the short link for iOS device targeting."""
    android: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('android'), 'exclude': lambda f: f is UpdateLinkRequestBody.UNSET }})
    r"""The Android destination URL for the short link for Android device targeting."""
    geo: Optional[components_linkgeotargeting.LinkGeoTargeting] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('geo'), 'exclude': lambda f: f is UpdateLinkRequestBody.UNSET }})
    r"""Geo targeting information for the short link in JSON format `{[COUNTRY]: https://example.com }`."""
    do_index: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('doIndex'), 'exclude': lambda f: f is None }})
    r"""Allow search engines to index your short link. Defaults to `false` if not provided. Learn more: https://d.to/noindex"""
    



@dataclasses.dataclass
class UpdateLinkRequest:
    link_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'linkId', 'style': 'simple', 'explode': False }})
    r"""The id of the link to update. You may use either `linkId` (obtained via `/links/info` endpoint) or `externalId` prefixed with `ext_`."""
    request_body: Optional[UpdateLinkRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    


UpdateLinkTagIds = Union[str, List[str]]

UpdateLinkTagNames = Union[str, List[str]]
